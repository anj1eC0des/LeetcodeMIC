# Flatten Binary Tree to Linked List

**Difficulty:** Medium  
**Submitted:** 2026-01-16 07:02 UTC  
**Submission ID:** 1886552324

---

## Test Cases

### Example 1

```
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
```

### Example 2

```
Input: root = []
Output: []
```

### Example 3

```
Input: root = [0]
Output: [0]
&nbsp;
```

## My Notes

- Definition for a binary tree node.
- public class TreeNode {
- int val;
- TreeNode left;
- TreeNode right;
- TreeNode() {}
- TreeNode(int val) { this.val = val; }
- TreeNode(int val, TreeNode left, TreeNode right) {
- this.val = val;
- this.left = left;
- this.right = right;
- }
- if no left child exists, just flatten right

---

*Last updated: 2026-01-31*
