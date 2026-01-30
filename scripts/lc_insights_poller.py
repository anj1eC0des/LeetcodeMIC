import os
import json
import re
import time
from pathlib import Path
from datetime import datetime, timezone

import requests

GRAPHQL = "https://leetcode.com/graphql"  # LeetCode GraphQL endpoint [1](https://github.com/topics/leetcode-api)

STATE_FILE = Path(".lc_state.json")
INSIGHTS_DIR = Path("insights")

# -----------------------
# Queries (from your DevTools payloads)
# -----------------------

RECENT_AC_QUERY = r"""
query recentAcSubmissions($username: String!, $limit: Int!) {
  recentAcSubmissionList(username: $username, limit: $limit) {
    id
    title
    titleSlug
    timestamp
  }
}
"""

SUBMISSION_DETAILS_QUERY = r"""
query submissionDetails($submissionId: Int!) {
  submissionDetails(submissionId: $submissionId) {
    code
    timestamp
    statusCode
    lang { name verboseName }
    question { titleSlug }
  }
}
"""
# statusCode 10 == Accepted in common LeetCode client mappings [4](https://codingsnack.github.io/leetcode-api/classes/graphql_helper.GraphQLHelper.html)[1](https://github.com/topics/leetcode-api)

# -----------------------
# GraphQL helper with retry/backoff
# -----------------------

def graphql_post(query, variables, session, csrf, tries=4):
    """
    Authenticated LeetCode GraphQL calls commonly require:
    - cookies: LEETCODE_SESSION + csrftoken
    - header: x-csrftoken
    - JSON body: { query, variables }
    [2](https://microsoftedge.microsoft.com/addons/detail/pfkmmfgbeofmmmfpfcbclmghklhmdhnf)[1](https://github.com/topics/leetcode-api)[3](https://deepwiki.com/wklee610/leetcode-cli/5.1-graphql-query-definitions)
    """
    headers = {
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com/",
        "x-csrftoken": csrf,
        "User-Agent": "Mozilla/5.0",
    }
    cookies = {
        "LEETCODE_SESSION": session,
        "csrftoken": csrf,
    }
    payload = {"query": query, "variables": variables}

    last_err = None
    for attempt in range(1, tries + 1):
        try:
            r = requests.post(
                GRAPHQL,
                headers=headers,
                cookies=cookies,
                json=payload,
                timeout=30
            )

            # Detect non-JSON response (can happen with bot protection pages)
            ctype = (r.headers.get("content-type") or "").lower()
            if "application/json" not in ctype:
                raise RuntimeError(
                    f"Non-JSON response (possible bot protection). status={r.status_code}"
                )

            r.raise_for_status()
            body = r.json()
            if "errors" in body:
                raise RuntimeError(body["errors"])
            return body["data"]

        except Exception as e:
            last_err = e
            sleep_s = min(60, 2 ** (attempt - 1))  # 1,2,4,8... up to 60s
            print(f"[WARN] GraphQL attempt {attempt}/{tries} failed: {e}. Retrying in {sleep_s}s...")
            time.sleep(sleep_s)

    raise RuntimeError(f"GraphQL failed after {tries} tries: {last_err}")

# -----------------------
# Java comment extraction (// and /* */)
# -----------------------

RE_BLOCK = re.compile(r"/\*.*?\*/", re.DOTALL)
RE_LINE = re.compile(r"^\s*//(.*)$", re.MULTILINE)

def extract_java_comments(code: str):
    comments = []

    # /* ... */ blocks
    for m in RE_BLOCK.finditer(code):
        blk = m.group(0)
        blk = re.sub(r"^/\*+|\*+/$", "", blk.strip())
        for line in blk.splitlines():
            line = re.sub(r"^\s*\*\s?", "", line).strip()
            if line:
                comments.append(line)

    # // single-line
    for m in RE_LINE.finditer(code):
        line = m.group(1).strip()
        if line:
            comments.append(line)

    # De-dupe preserve order
    seen = set()
    out = []
    for c in comments:
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out

# -----------------------
# Markdown writing (overwrite per problem slug)
# -----------------------

def write_card(slug, title, submission_id, submitted_ts, comments):
    INSIGHTS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = INSIGHTS_DIR / f"{slug}.md"

    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    submitted_at = datetime.fromtimestamp(int(submitted_ts), tz=timezone.utc).isoformat()

    front = (
        f"---\n"
        f"problem: {title}\n"
        f"slug: {slug}\n"
        f"language: Java\n"
        f"submission_id: {submission_id}\n"
        f"submitted_at_utc: {submitted_at}\n"
        f"updated: {updated}\n"
        f"---\n\n"
    )

    body = "## Notes (from Java code comments)\n"
    if comments:
        body += "\n".join([f"- {c}" for c in comments]) + "\n"
    else:
        body += "- (No comments found)\n"

    out_path.write_text(front + body, encoding="utf-8")

def update_index():
    if not INSIGHTS_DIR.exists():
        return
    files = sorted([p for p in INSIGHTS_DIR.glob("*.md") if p.name != "README.md"])
    lines = ["# Insight Cards\n"]
    for p in files:
        txt = p.read_text(encoding="utf-8")
        m = re.search(r"^problem:\s*(.*)$", txt, re.MULTILINE)
        title = m.group(1).strip() if m else p.stem
        lines.append(f"- {title}")
    (INSIGHTS_DIR / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

# -----------------------
# State (avoid reprocessing same submission IDs)
# -----------------------

def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {"seen_submission_ids": []}

def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")

# -----------------------
# Main
# -----------------------

def main():
    session = os.environ.get("LEETCODE_SESSION", "").strip()
    csrf = os.environ.get("LEETCODE_CSRF", "").strip()
    username = os.environ.get("LEETCODE_USERNAME", "").strip()
    limit = int(os.environ.get("LC_LIMIT", "100"))
    backfill = os.environ.get("LC_BACKFILL", "0").strip() == "1"

    if not session or not csrf:
        raise SystemExit("Missing env vars: LEETCODE_SESSION and/or LEETCODE_CSRF")
    if not username:
        raise SystemExit("Missing env var: LEETCODE_USERNAME")

    state = load_state()
    seen = set(map(int, state.get("seen_submission_ids", [])))

    # 1) Pull recent accepted submissions (AC-only list)
    data = graphql_post(
        RECENT_AC_QUERY,
        {"username": username, "limit": limit},
        session=session,
        csrf=csrf
    )
    recents = data.get("recentAcSubmissionList") or []

    if backfill:
        print(f"[INFO] Backfill ON: regenerating cards for last {len(recents)} accepted submissions.")
        items_to_process = recents[:]  # regenerate for all returned
    else:
        items_to_process = [it for it in recents if int(it["id"]) not in seen]

    # Oldest → newest for stable updates
    items_to_process.sort(key=lambda x: int(x.get("timestamp", "0")))

    print(f"[INFO] Recent accepted returned={len(recents)}; processing={len(items_to_process)}; limit={limit}; backfill={backfill}")

    # 2) For each (new) accepted submission, fetch details and generate card
    processed = 0
    for it in items_to_process:
        sid = int(it["id"])
        title = it.get("title") or it.get("titleSlug") or "Unknown"
        slug = it.get("titleSlug") or "unknown"
        ts = it.get("timestamp") or "0"

        print(f"[INFO] Processing submissionId={sid} slug={slug} title={title}")

        details_data = graphql_post(
            SUBMISSION_DETAILS_QUERY,
            {"submissionId": sid},
            session=session,
            csrf=csrf
        )
        details = details_data.get("submissionDetails") or {}

        # Optional sanity check: accepted == 10 [4](https://codingsnack.github.io/leetcode-api/classes/graphql_helper.GraphQLHelper.html)[1](https://github.com/topics/leetcode-api)
        status = details.get("statusCode")
        if status is not None and int(status) != 10:
            print(f"[WARN] Skipping submissionId={sid} because statusCode={status} (not Accepted)")
            seen.add(sid)
            continue

        code = details.get("code") or ""
        comments = extract_java_comments(code)

        if not comments:
            print(f"[INFO] No comments found for submissionId={sid} ({slug})")

        write_card(slug, title, sid, ts, comments)
        seen.add(sid)
        processed += 1

        # be polite to the endpoint
        time.sleep(1)

    state["seen_submission_ids"] = sorted(seen)
    save_state(state)
    update_index()

    print(f"[INFO] Done. Cards updated={processed}. Total seen submission IDs={len(seen)}.")

if __name__ == "__main__":
    main()