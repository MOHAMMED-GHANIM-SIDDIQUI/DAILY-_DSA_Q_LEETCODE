# 3634. Count Partitions with Max-Min Difference at Most K

## 🔗 Problem Link
https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Sorting, Sliding Window, Greedy

---

## 🧩 Problem Summary
Given an array `nums` and an integer `k`, find the minimum number of elements to remove so that the ratio between the maximum and minimum element in the remaining array is at most `k`. Equivalently, find the longest subarray (after sorting) where `max <= k * min`, and return `n - length`.

### 📌 Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= 10^9`

---

## 💭 Intuition
👉 Sort the array, then use a sliding window to find the longest subarray where `nums[j] <= k * nums[i]` — the answer is `n` minus this longest window length.

---

## ⚡ Approach — Sort + Sliding Window

### 🧠 Idea
- Sort the array so the smallest and largest in any window are at the endpoints.
- Use two pointers: for each right endpoint `j`, advance left pointer `i` until `nums[j] <= k * nums[i]`.
- Track the maximum window length.
- Answer = `n - maxLength`.

---

## 💻 Code

```python
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        L = 1
        i = 0

        for j in range(n):
            maxEl = nums[j]

            while i < j and maxEl > k * nums[i]:
                i += 1

            L = max(L, j - i + 1)

        return n - L
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 3, 5, 7, 9], k = 2
```
### Steps
```
Sorted: [1, 3, 5, 7, 9]

j=0: maxEl=1, i=0, window=[1], L=1
j=1: maxEl=3, 3<=2*1? No → i=1, window=[3], L=1
j=2: maxEl=5, 5<=2*3? Yes, window=[3,5], L=2
j=3: maxEl=7, 7<=2*3? No → i=2, 7<=2*5? Yes, window=[5,7], L=2
j=4: maxEl=9, 9<=2*5? No → i=3, 9<=2*7? Yes, window=[7,9], L=2

Result: 5 - 2 = 3
```

---

## ⏱️ Time Complexity
```
O(n log n) — dominated by sorting; the sliding window is O(n)
```

## 💾 Space Complexity
```
O(1) — sorting in-place, only using pointers
```

---

## ⚠️ Edge Cases
- All elements are equal → remove 0
- k = 1 → only identical elements can remain
- Single element → remove 0
- Very large values → watch for overflow in `k * nums[i]`

---

## 🎯 Interview Takeaways
- Sorting transforms a "subset" problem into a "subarray" problem.
- Two-pointer / sliding window on sorted arrays is extremely powerful.
- Always consider whether "longest valid subarray after sorting" solves your problem.

---

## 📌 Key Pattern
👉 **"Sort + sliding window to find the longest subarray satisfying a min/max ratio constraint."**

---

## 🔁 Related Problems
- 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
- 2779. Maximum Beauty of an Array After Applying Operation
- 1984. Minimum Difference Between Highest and Lowest of K Scores

---

## 🚀 Final Thoughts
This problem reduces to finding the longest "valid" window after sorting, where the ratio constraint is checked at the window endpoints. The sliding window approach is optimal and elegant.

---

✨ **Rule to remember:**
> "Sort first, then slide a window — the longest valid window gives the minimum removals."
