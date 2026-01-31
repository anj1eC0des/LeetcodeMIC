# Implement Trie (Prefix Tree)

**Difficulty:** Medium  
**Submitted:** 2026-01-31 14:26 UTC  
**Submission ID:** 1903075932

---

## Test Cases

### Example 1

```
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]
Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
```

## My Notes

- Trie class needs a map of tries, representing letters and a boolean field
- "isWord" denoting if the trie denotes the last letter of a word.
- void insert(String word) checks letters by going along the letters in map[]
- and inserts letters where its needed and sets the isWord of trie representing final
- letter to be true.
- boolean search(String word) just iterates along the map[]s and
- checks if the letters are mapped in order and the ending letter has isWord.
- boolean startsWith(String word) is same as search, but doesnt care for isWord.

---

*Last updated: 2026-01-31*
