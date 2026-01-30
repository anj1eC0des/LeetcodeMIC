---
problem: Implement Trie (Prefix Tree)
slug: implement-trie-prefix-tree
language: Java
submission_id: 1902048202
submitted_at_utc: 2026-01-30T14:09:41+00:00
updated: 2026-01-30
---

## Notes (from Java code comments)
- Your Trie object will be instantiated and called as such:
- Trie obj = new Trie();
- obj.insert(word);
- boolean param_2 = obj.search(word);
- boolean param_3 = obj.startsWith(prefix);
- Trie class needs a map of tries, representing letters and a boolean field
- "isWord" denoting if the trie denotes the last letter of a word.
- void insert(String word) checks letters by going along the letters in map[]
- and inserts letters where its needed and sets the isWord of trie representing final
- letter to be true.
- boolean search(String word) just iterates along the map[]s and
- checks if the letters are mapped in order and the ending letter has isWord.
- boolean startsWith(String word) is same as search, but doesnt care for isWord.
