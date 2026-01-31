# Flatten Nested List Iterator

**Difficulty:** Medium  
**Submitted:** 2026-01-16 11:05 UTC  
**Submission ID:** 1886724307

---

## Test Cases

### Example 1

```
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
```

### Example 2

```
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
&nbsp;
```

## My Notes

- // This is the interface that allows for creating nested lists.
- // You should not implement it, or speculate about its implementation
- public interface NestedInteger {
- // @return true if this NestedInteger holds a single integer, rather than a nested list.
- public boolean isInteger();
- // @return the single integer that this NestedInteger holds, if it holds a single integer
- // Return null if this NestedInteger holds a nested list
- public Integer getInteger();
- // @return the nested list that this NestedInteger holds, if it holds a nested list
- // Return empty list if this NestedInteger holds a single integer
- public List<NestedInteger> getList();
- }
- Your NestedIterator object will be instantiated and called as such:
- NestedIterator i = new NestedIterator(nestedList);
- while (i.hasNext()) v[f()] = i.next();
- System.out.println(flattendList);

---

*Last updated: 2026-01-31*
