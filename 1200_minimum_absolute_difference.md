# 1200. Minimum Absolute Difference

## 🔗 Problem Link
https://leetcode.com/problems/minimum-absolute-difference/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Sorting

---

## 🧩 Problem Summary

Given an array of distinct integers, find all pairs of elements with the minimum absolute difference. Return a list of pairs in ascending order, where each pair is also sorted in ascending order.

### 📌 Constraints
- `2 <= arr.length <= 10^5`
- `-10^6 <= arr[i] <= 10^6`

---

## 💭 Intuition

👉 The minimum absolute difference can only occur between adjacent elements in a sorted array. Sort first, then find the minimum gap and collect all pairs with that gap.

---

## ⚡ Approach — Sort and Two-Pass Scan

### 🧠 Idea
- Sort the array.
- First pass: find the minimum difference between consecutive elements.
- Second pass: collect all consecutive pairs whose difference equals the minimum.

---

## 💻 Code

```python
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff= float('inf')
        for i in range(len(arr)-1):
            cur_diff = arr[i+1] - arr[i]
            if cur_diff < min_diff:
                min_diff = cur_diff
        ans = []
        for i in range(len(arr)-1):
            cur_diff = arr[i+1] - arr[i]
            if cur_diff == min_diff:
                ans.append([arr[i] , arr[i+1]])
        return ans
```

---

## 🧠 Dry Run

### Input
```
arr = [4, 2, 1, 3]
```

### Steps
```
After sort: [1, 2, 3, 4]

Pass 1 — find min_diff:
  i=0: 2-1=1, min_diff=1
  i=1: 3-2=1, min_diff=1
  i=2: 4-3=1, min_diff=1

Pass 2 — collect pairs with diff=1:
  i=0: [1,2] ✓
  i=1: [2,3] ✓
  i=2: [3,4] ✓

Output: [[1,2],[2,3],[3,4]]
```

---

## ⏱️ Time Complexity
```
O(n log n)
```
Dominated by the sorting step. The two linear passes are O(n).

---

## 💾 Space Complexity
```
O(1)
```
Excluding the output array and sort space, only a few variables are used.

---

## ⚠️ Edge Cases
- Two elements → only one pair, which is the answer.
- All elements equally spaced → every consecutive pair is in the answer.
- Large negative and positive numbers → difference computation still works with standard int.

---

## 🎯 Interview Takeaways
- Sorting transforms "minimum absolute difference" into "minimum adjacent difference."
- Two-pass approach is cleaner than single-pass with result replacement.
- The result is automatically sorted since the input is sorted.
- This is a great warm-up problem for sorting-based techniques.

---

## 📌 Key Pattern
👉 **"Sort first — minimum absolute difference always occurs between adjacent elements in sorted order."**

---

## 🔁 Related Problems
- 532 - K-diff Pairs in an Array
- 908 - Smallest Range I
- 2144 - Minimum Cost of Buying Candies With Discount

---

## 🚀 Final Thoughts
A straightforward sorting problem that illustrates why sorting is so powerful — it converts a global property (minimum difference across all pairs) into a local one (adjacent differences).

---

✨ **Rule to remember:**
> "After sorting, the closest pair is always adjacent — no need to check all O(n^2) pairs."
