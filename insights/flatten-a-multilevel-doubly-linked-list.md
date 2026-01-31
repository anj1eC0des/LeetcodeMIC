# Flatten a Multilevel Doubly Linked List

**Difficulty:** Medium  
**Submitted:** 2026-01-19 11:37 UTC  
**Submission ID:** 1889796069

---

## Test Cases

### Example 1

```
Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation: The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:
```

### Example 2

```
Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation: The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:
```

### Example 3

```
Input: head = []
Output: []
Explanation: There could be empty list in the input.
&nbsp;
```

## My Notes

- // Definition for a Node.
- class Node {
- public int val;
- public Node prev;
- public Node next;
- public Node child;
- };
- Definition for a Node.

---

*Last updated: 2026-01-31*
