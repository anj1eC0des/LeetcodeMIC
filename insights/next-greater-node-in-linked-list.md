# Next Greater Node In Linked List

**Difficulty:** Medium  
**Submitted:** 2026-02-03 07:01 UTC  
**Submission ID:** 1906381489

---

## Test Cases

### Example 1

```
Input: head = [2,1,5]
Output: [5,5,0]
```

### Example 2

```
Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]
```

## My Notes

- If you could iterate in reverse, its the same as next greater element in a list. But for singly linked list, we cant do it.
- We need to save the elements in list for quick look up by index. Have a stack. Iterate and add node indices to the stack, when you find an element greater than current element, pop all indicies that are less than current element.

---

*Last updated: 2026-02-03*
