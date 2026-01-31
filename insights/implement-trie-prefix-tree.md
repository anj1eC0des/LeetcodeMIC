# Implement Trie (Prefix Tree)

**Difficulty:** Medium  
**Submitted:** 2026-01-30 14:09 UTC  
**Submission ID:** 1902048202

---

## Test Cases

### Example 1

```
Input
[&quot;Trie&quot;, &quot;insert&quot;, &quot;search&quot;, &quot;search&quot;, &quot;startsWith&quot;, &quot;insert&quot;, &quot;search&quot;]
[[], [&quot;apple&quot;], [&quot;apple&quot;], [&quot;app&quot;], [&quot;app&quot;], [&quot;app&quot;], [&quot;app&quot;]]
Output
[null, null, true, false, true, null, true]
Explanation
Trie trie = new Trie();
trie.insert(&quot;apple&quot;);
trie.search(&quot;apple&quot;);   // return True
trie.search(&quot;app&quot;);     // return False
trie.startsWith(&quot;app&quot;); // return True
trie.insert(&quot;app&quot;);
trie.search(&quot;app&quot;);     // return True
&nbsp;
```

## My Notes

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

---

*Last updated: 2026-01-31*
