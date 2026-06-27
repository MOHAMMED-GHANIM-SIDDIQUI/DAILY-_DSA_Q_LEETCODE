# 2130. Maximum Twin Sum of a Linked List

## 🔗 Problem Link
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Linked List, Two Pointers, Stack

---

## 🧩 Problem Summary

In a linked list of **even** size `n`, the node at 0-indexed position `i` is the **twin** of the node at position `n - 1 - i`, for `0 <= i < n/2`. The **twin sum** is the sum of a node and its twin's values. Return the **maximum** twin sum across all twin pairs.

### 📌 Constraints
- The number of nodes is an **even** integer in the range `[2, 10^5]`.
- `1 <= Node.val <= 10^5`.

---

## 💭 Intuition

👉 Twin pairs are symmetric around the center, exactly like pairing the first and last elements of an array and walking inward. The simplest way to get random access to position `n - 1 - i` from a linked list is to copy all values into a Python list, then pair index `i` with index `n - 1 - i` and track the maximum sum.

---

## ⚡ Approach — Copy to Array, Pair Inward

### 🧠 Idea
- Traverse the list, appending every `val` into `my_list`.
- Let `n = len(my_list)`.
- For each `i` in `[0, n/2)`, compute `my_list[i] + my_list[n-1-i]` (the twin sum).
- Keep a running `ans = max(ans, twin_sum)`.
- Return `ans`.

---

## 💻 Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        my_list = []
        temp = head
        while temp:
            my_list .append(temp.val)
            temp= temp.next
        n = len(my_list)
        ans = 0
        for i in range(n//2):
            ans = max(ans , my_list[i] + my_list[n-1-i])
        return ans
```

---

## 🧠 Dry Run

### Input
```
head = [5, 4, 2, 1]   (n = 4)
```

### Steps
```
Copy values -> my_list = [5, 4, 2, 1], n = 4
ans = 0
i = 0: twin = my_list[0] + my_list[3] = 5 + 1 = 6 -> ans = max(0, 6) = 6
i = 1: twin = my_list[1] + my_list[2] = 4 + 2 = 6 -> ans = max(6, 6) = 6
return 6
```

---

## ⏱️ Time Complexity
```
O(n)
```
One pass to copy values into the array, plus `n/2` iterations to compute twin sums — linear overall.

---

## 💾 Space Complexity
```
O(n)
```
The auxiliary array stores all `n` node values. (This can be reduced to `O(1)` by reversing the second half in place.)

---

## ⚠️ Edge Cases
- Minimum size `n = 2`: single twin pair `(my_list[0], my_list[1])`.
- The list length is guaranteed even, so `n // 2` exactly covers every twin without a middle leftover.
- All values are positive, so initializing `ans = 0` is safe.

---

## 🎯 Interview Takeaways
- Twin pairs = symmetric two-pointer pairing; copying to an array makes the symmetry trivial.
- Mention the `O(1)`-space follow-up: find the middle with slow/fast pointers, reverse the second half, then walk both halves together.
- Random access is the linked-list weakness this problem exploits.

---

## 📌 Key Pattern
👉 **"Flatten to an array when you need symmetric (i, n-1-i) access on a linked list."**

---

## 🔁 Related Problems
- 234. Palindrome Linked List
- 876. Middle of the Linked List
- 206. Reverse Linked List
- 2095. Delete the Middle Node of a Linked List

---

## 🚀 Final Thoughts
Copying to an array trades `O(n)` space for clarity and is perfectly acceptable. The optimal `O(1)`-space solution combines three classic linked-list techniques — find middle, reverse half, two-pointer walk — making this a great problem to demonstrate that progression in an interview.

---

✨ **Rule to remember:**
> "Symmetric pairing is easiest on an array; reverse-the-second-half is how you do it in O(1) space."
