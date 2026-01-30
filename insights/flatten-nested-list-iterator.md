---
problem: Flatten Nested List Iterator
slug: flatten-nested-list-iterator
language: Java
submission_id: 1886724307
submitted_at_utc: 2026-01-16T11:05:58+00:00
updated: 2026-01-30
---

## Notes (from Java code comments)
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
