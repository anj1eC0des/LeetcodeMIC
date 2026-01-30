---
problem: Flatten Binary Tree to Linked List
slug: flatten-binary-tree-to-linked-list
language: Java
submission_id: 1886552324
submitted_at_utc: 2026-01-16T07:02:08+00:00
updated: 2026-01-30
---

## Notes (from Java code comments)
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
