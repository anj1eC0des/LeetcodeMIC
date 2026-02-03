# Word Search II

**Difficulty:** Hard  
**Submitted:** 2026-02-03 06:41 UTC  
**Submission ID:** 1906360429

---

## Test Cases

### Example 1

```
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

### Example 2

```
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
```

## My Notes

- Backtracking problem where the success condition is determined by trie.
- To really build performance for this there were two insights that are important.
- Build the trie for all the words that you have to match. While scanning the matrix, recursively try and find matching words when you find a starting letter.
- You iterate and you find a word. Now this word need not be added again to the result since we dont need duplicates. So we can set the isWord of the last character of the word as false.
- Now consider this scenario, this trie for the word that is already matched and invalidated is actually useless unless it is a prefix to a word that is yet to be matched. We can just ignore if its the later case, otherwise, we have to prune this branch.
- If a letter is the last letter of a matched word and not a prefix of another word,i.e., its already recorded in result set and its map is empty, we can remove this letter from the mapping of the parent trie, since tracing this branch is of no use to us. Doing this recursively prunes all the unwanted branches. To aid this add an isEmpty() method to the trie definition.

---

*Last updated: 2026-02-03*
