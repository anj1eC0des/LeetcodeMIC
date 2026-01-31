# Linked List Components

**Difficulty:** Medium  
**Submitted:** 2026-01-20 15:16 UTC  
**Submission ID:** 1891145463

---

## Test Cases

### Example 1

```
Input: head = [0,1,2,3], nums = [0,1,3]
Output: 2
Explanation: 0 and 1 are connected, so [0, 1] and [3] are the two connected components.
```

### Example 2

```
Input: head = [0,1,2,3,4], nums = [0,3,1,4]
Output: 2
Explanation: 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
&nbsp;
```

## My Notes

- Definition for singly-linked list.
- public class ListNode {
- int val;
- ListNode next;
- ListNode() {}
- ListNode(int val) { this.val = val; }
- ListNode(int val, ListNode next) { this.val = val; this.next = next; }
- }

---

*Last updated: 2026-01-31*
