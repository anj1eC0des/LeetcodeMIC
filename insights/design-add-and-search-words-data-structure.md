# Design Add and Search Words Data Structure

**Difficulty:** Medium  
**Submitted:** 2026-02-03 08:06 UTC  
**Submission ID:** 1906435794

---

## Test Cases

*No example test cases extracted*

## My Notes

- Classic trie problem, build Trie, which contains map[] of tries and isWord fields, and addWord and searchWord method
- addWord()- iterate the characters in the word to be added. from the current trie if a mapping exists to the trie representing the current letter, select that trie as the current trie, else create a trie, map it and then select it. for the last letter, turn isWord as true
- search()- moving along the trie, if a letter mapping doesn't exist for the letter to be matched return false. if the matching does exist but isWord for last letter is false in trie, return false. otherwise keep matching and return true if isWord is true at the end.

---

*Last updated: 2026-02-03*
