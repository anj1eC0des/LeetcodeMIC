# Permutation in String

**Difficulty:** Medium  
**Submitted:** 2026-02-03 08:29 UTC  
**Submission ID:** 1906454954

---

## Test Cases

### Example 1

```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

### Example 2

```
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```

## My Notes

- Its a nice sliding window problem. We iterate along the characters.
- While we keep finding chars from the other string we decrease their count in the count array, and we keep doing it the count of the current element is 0(which maybe because the char doesnt exist in the other string or the count is exhauted while matching.)
- We check if all the count array is empty - all chars from other string have been matched and a permutation has been found. If it is we return true.
- Else we have to add the chars back in the count array based on the loop exit condition. If the loop exit because of char not being found, we just dump all the chars scanned till now, else we dump chars till the count of current char is non-zero, that way we can continue matching.

---

*Last updated: 2026-02-03*
