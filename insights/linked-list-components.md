# Linked List Components

**Difficulty:** Medium  
**Submitted:** 2026-02-03 07:38 UTC  
**Submission ID:** 1906414566

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
```

## My Notes

- Consecutive nodes with values in the nums set belong in one component.
- We keep considering elements to be in the same component as long as they are consecutive and blong to nums set, else we consider it another component. we return the component count.

---

*Last updated: 2026-02-03*
