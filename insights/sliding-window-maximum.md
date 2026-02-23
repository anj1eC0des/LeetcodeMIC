# Sliding Window Maximum

**Difficulty:** Hard  
**Submitted:** 2026-02-23 09:55 UTC  
**Submission ID:** 1928353821

---

## Test Cases

### Example 1

```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
1 [3  -1  -3] 5  3  6  7       3
1  3 [-1  -3  5] 3  6  7       5
1  3  -1 [-3  5  3] 6  7       5
1  3  -1  -3 [5  3  6] 7       6
1  3  -1  -3  5 [3  6  7]      7
```

### Example 2

```
Input: nums = [1], k = 1
Output: [1]
```

## My Notes

*No comments found in submission*

---

*Last updated: 2026-02-23*
