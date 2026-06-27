# 2095. Delete the Middle Node of a Linked List

## 🔗 Problem Link
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Linked List, Two Pointers

---

## 🧩 Problem Summary

You are given the `head` of a singly linked list. Delete the **middle node** and return the head of the modified list. The middle node of a list of size `n` is the `⌊n/2⌋`-th node (0-indexed), where `⌊x⌋` denotes the floor function. If the list has a single node, deleting the middle leaves an empty list, so return `None`.

### 📌 Constraints
- The number of nodes is in the range `[1, 10^5]`.
- `1 <= Node.val <= 10^5`.

---

## 💭 Intuition

👉 The middle index is `n // 2`. To unlink a node from a singly linked list, you must stand on its **predecessor**. So first measure the length `n`, then walk `n//2 - 1` steps from the head to land on the node just before the middle, and splice the middle out with `temp.next = temp.next.next`. The only special case is `n == 1`, where the middle is the head itself and the result is empty.

---

## ⚡ Approach — Count Length then Skip to Predecessor

### 🧠 Idea
- First pass: traverse the whole list counting nodes into `n`.
- If `n == 1`, the only node is the middle → return `None`.
- Reset `temp` to `head` and advance `n // 2 - 1` steps to reach the predecessor of the middle node.
- Bypass the middle node: `temp.next = temp.next.next`.
- Return `head`.

---

## 💻 Code

```python
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        temp = head

        while temp:
            n += 1
            temp = temp.next

        if n == 1:
            return None

        temp = head
        for _ in range(n // 2 - 1):
            temp = temp.next

        temp.next = temp.next.next

        return head
```

---

## 🧠 Dry Run

### Input
```
head = [1, 3, 4, 7, 1, 2, 6]   (n = 7, middle index = 7//2 = 3 -> value 7)
```

### Steps
```
First pass counts n = 7.
n != 1, so proceed.
Reset temp = head (node 1).
Loop runs n//2 - 1 = 3 - 1 = 2 times:
  iter 1: temp = node 3
  iter 2: temp = node 4   (predecessor of middle)
temp.next = temp.next.next  ->  node 4 now points to node 1 (skipping node 7)
Result: [1, 3, 4, 1, 2, 6]
return head
```

---

## ⏱️ Time Complexity
```
O(n)
```
One full pass to count the length, plus up to ~n/2 steps to reach the predecessor — linear overall.

---

## 💾 Space Complexity
```
O(1)
```
Only a counter and a pointer are used; the list is modified in place.

---

## ⚠️ Edge Cases
- Single node (`n == 1`): returns `None`.
- Two nodes (`n == 2`): middle index `1`; loop runs `0` times, head stays the predecessor and the second node is removed.
- Odd vs even length both handled by `n // 2` (floor) middle definition.

---

## 🎯 Interview Takeaways
- To delete a node in a singly linked list you need its predecessor.
- A two-pass (count then walk) solution is simple and `O(1)` space.
- A slow/fast pointer variant deletes the middle in a single pass — good follow-up to mention.

---

## 📌 Key Pattern
👉 **"Stop one node before the target to splice it out."**

---

## 🔁 Related Problems
- 876. Middle of the Linked List
- 19. Remove Nth Node From End of List
- 237. Delete Node in a Linked List
- 2130. Maximum Twin Sum of a Linked List

---

## 🚀 Final Thoughts
This is a clean introduction to pointer surgery on linked lists. Counting the length first avoids the cognitive overhead of slow/fast pointers, at the cost of a second traversal. Both approaches are `O(n)` time and `O(1)` space, so either is acceptable; the explicit-count version is often easier to reason about and debug under interview pressure.

---

✨ **Rule to remember:**
> "To remove a node, always grab the one before it — `prev.next = prev.next.next`."
