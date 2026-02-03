# Trapping Rain Water

**Difficulty:** Hard  
**Submitted:** 2026-02-03 07:48 UTC  
**Submission ID:** 1906422599

---

## Test Cases

### Example 1

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

### Example 2

```
Input: height = [4,2,0,3,2,5]
Output: 9
```

## My Notes

- Water can be trappedn at a point if there are structures bigger than current height on the either side. How much water can be trapped depends on the minimum of either heights.
- Looking at the test-case, we might be tempted to find the first element larger than current height on either side, but global min and max values to either side suffice, with water trapped being min(leftMax,rightMax)-currentHeight.

---

*Last updated: 2026-02-03*
