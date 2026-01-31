# Binary Tree Pruning

**Difficulty:** Medium  
**Submitted:** 2026-01-12 11:14 UTC  
**Submission ID:** 1882699596

---

## Test Cases

### Example 1

```
Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation:
Only the red nodes satisfy the property &quot;every subtree not containing a 1&quot;.
The diagram on the right represents the answer.
```

### Example 2

```
Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]
```

### Example 3

```
Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]
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

---

*Last updated: 2026-01-31*
