# Split Linked List in Parts

**Difficulty:** Medium  
**Submitted:** 2026-01-21 07:25 UTC  
**Submission ID:** 1891873068

---

## Test Cases

### Example 1

```
Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].
```

### Example 2

```
Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
&nbsp;
```

## My Notes

- Definition for singly-linked list.
- public class ListNode {
- int val;
- ListNode next;
- ListNode() {}
- ListNode(int val) { this.val = val; }
- ListNode(int val, ListNode next) { this.val = val; this.next = next; }
- }
- System.out.println(n);
- for(ListNode l:ans) System.out.print(l==null?"null":l.val+" ");
- System.out.println();
- System.out.println(n+" "+k);
- System.out.println(l);

---

*Last updated: 2026-01-31*
