# 3740. Find the Key of the Numbers

## 🔗 Problem Link
https://leetcode.com/problems/find-the-key-of-the-numbers/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, Sorting

---

## 🧩 Problem Summary
Given an array `nums`, find the minimum "good distance." A "good distance" for a value requires at least 3 occurrences (indices). For each triplet of consecutive occurrences `(idx[i], idx[i+1], idx[i+2])`, the good distance is the sum of all pairwise differences. Return the minimum across all values, or `-1` if no value appears at least 3 times.

### 📌 Constraints
- `1 <= len(nums) <= 10^5`
- `1 <= nums[i] <= 10^9`

---

## 💭 Intuition
👉 Group indices by value. For any three consecutive indices `a, b, c`, the total pairwise distance is `(b-a) + (c-b) + (c-a) = 2*(c-a)`. The minimum is achieved by the tightest triplet of consecutive occurrences.

---

## ⚡ Approach — Hash Map Grouping with Sliding Triplet

### 🧠 Idea
- Build a dictionary mapping each value to its list of indices (in order of appearance).
- For each value with at least 3 occurrences, slide a window of size 3 over consecutive indices.
- Compute the good distance as `(idx[i+1] - idx[i]) + (idx[i+2] - idx[i+1]) + (idx[i+2] - idx[i])`.
- Track the global minimum.

---

## 💻 Code

```python
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        tracker = defaultdict(list)
        min_good_dist = float('inf')
        for idx , val in enumerate(nums):
          tracker[val].append(idx)
        for key , idx_list in tracker.items():
          if len(idx_list) >= 3:
            n = len(idx_list)
            for i in range(n-2):
              cur_good_dist = (idx_list[i+1] - idx_list[i]) + (idx_list[i+2] - idx_list[i+1]) + (idx_list[i+2] - idx_list[i])
              if cur_good_dist < min_good_dist:
                min_good_dist = cur_good_dist
        return -1 if min_good_dist == float('inf') else min_good_dist
```

---

## 🧠 Dry Run
### Input
```
nums = [1, 2, 1, 2, 1, 2]
```
### Steps
```
tracker = {1: [0, 2, 4], 2: [1, 3, 5]}

For value 1, idx_list = [0, 2, 4]:
  i=0: (2-0) + (4-2) + (4-0) = 2 + 2 + 4 = 8
  min_good_dist = 8

For value 2, idx_list = [1, 3, 5]:
  i=0: (3-1) + (5-3) + (5-1) = 2 + 2 + 4 = 8
  min_good_dist = 8

Result: 8
```

---

## ⏱️ Time Complexity
```
O(n) — each index is processed once for grouping, and each triplet is checked once
```

## 💾 Space Complexity
```
O(n) — for the hash map storing all indices
```

---

## ⚠️ Edge Cases
- No value appears 3 or more times → return `-1`
- All elements are the same → check consecutive triplets of the entire index list
- Very large values of `nums[i]` → no issue since we only store indices
- Array of length < 3 → always returns `-1`

---

## 🎯 Interview Takeaways
- Grouping indices by value is a fundamental technique for problems involving repeated elements.
- The good distance formula simplifies to `2 * (idx[i+2] - idx[i])`, so minimizing it means finding the closest triplet of consecutive occurrences.
- Using `defaultdict(list)` keeps the code clean and avoids key-existence checks.

---

## 📌 Key Pattern
👉 **"Group indices by value, then slide a fixed-size window over each group to find optimal triplets."**

---

## 🔁 Related Problems
- 2815. Max Pair Sum in an Array
- 2364. Count Number of Bad Pairs
- 532. K-diff Pairs in an Array

---

## 🚀 Final Thoughts
This problem reduces to index grouping and sliding window over triplets. The key simplification is recognizing that the sum of all three pairwise distances among three consecutive indices equals `2 * (last - first)`, so only the span of the triplet matters. This makes the solution both efficient and elegant.

---

✨ **Rule to remember:**
> "Group indices by value and slide a triplet window — the minimum span gives the minimum good distance."
