# Sliding Window Maximum

**Difficulty:** Hard  
**Submitted:** 2026-01-27 09:46 UTC  
**Submission ID:** 1898425098

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
&nbsp;
```

## My Notes

- System.out.println("arr[i-1] is "+arr[i-1]);
- System.out.println(map);
- System.out.println("removed <- "+arr[i-1]);
- System.out.println("put -> "+ arr[i+k-1]);

---

*Last updated: 2026-01-31*
