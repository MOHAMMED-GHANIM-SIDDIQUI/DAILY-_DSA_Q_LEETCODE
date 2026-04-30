# 961. N-Repeated Element in Size 2N Array

## 🔗 Problem Link
https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Hash Table

---

## 🧩 Problem Summary

You are given an integer array `nums` with `2n` elements. Exactly `n + 1` elements are unique, and exactly one element is repeated `n` times. Return the element that is repeated `n` times.

### 📌 Constraints
- `2 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^4`
- `nums.length == 2 * n` for some integer `n`

---

## 💭 Intuition

Since one element appears `n` times and there are `2n` elements total with `n+1` unique values, the repeated element is the first one we see twice. 👉 Simply iterate and check if we have seen the element before.

---

## ⚡ Approach — First Duplicate Detection

### 🧠 Idea

- Maintain a list (or set) of seen elements.
- For each element in nums, check if it is already in the seen collection.
- If yes, return it immediately — it must be the n-repeated element.

---

## 💻 Code

```python
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        my_list = []
        for i in nums:
            if i in my_list:

                return i
            my_list.append(i)
```

---

## 🧠 Dry Run

### Input
```
nums = [1, 2, 3, 3]
```

### Steps
```
i=1: my_list=[] → not found → my_list=[1]
i=2: my_list=[1] → not found → my_list=[1,2]
i=3: my_list=[1,2] → not found → my_list=[1,2,3]
i=3: my_list=[1,2,3] → found! → return 3
```

---

## ⏱️ Time Complexity

```
O(n)
```

In the worst case we check at most n+1 elements before finding the duplicate (since there are only n+1 unique values).

---

## 💾 Space Complexity

```
O(n)
```

For the list storing seen elements. Note: using a set instead of a list would improve the lookup from O(n) to O(1).

---

## ⚠️ Edge Cases

- **Minimum size:** `nums = [1, 1]` → returns 1 immediately
- **Repeated at the end:** `nums = [1, 2, 3, 2]` → still finds the duplicate
- **All same except one:** `nums = [5, 1, 5, 5]` → returns 5

---

## 🎯 Interview Takeaways

- Using a set instead of a list would make lookups O(1) instead of O(n) per check.
- The problem guarantees exactly one element repeats, so the first duplicate must be the answer.
- This is a classic "find duplicate" pattern — simple but tests understanding of data structures.

---

## 📌 Key Pattern

👉 **"First duplicate detection — the repeated element is guaranteed to be the first one seen twice"**

---

## 🔁 Related Problems

- 217. Contains Duplicate
- 287. Find the Duplicate Number
- 136. Single Number

---

## 🚀 Final Thoughts

A simple problem that can be solved by finding the first duplicate. Using a set would be more efficient than a list for membership testing, but both work within the given constraints.

---

✨ **Rule to remember:**
> When one element dominates half the array, it is guaranteed to be the first duplicate you encounter.
