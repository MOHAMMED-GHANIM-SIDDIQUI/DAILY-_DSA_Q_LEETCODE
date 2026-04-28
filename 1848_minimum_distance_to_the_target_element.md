# 1848. Minimum Distance to the Target Element

## 🔗 Problem Link
https://leetcode.com/problems/minimum-distance-to-the-target-element/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Linear Search

---

## 🧩 Problem Summary
Given an integer array `nums`, a `target` value, and an integer `start`, return the minimum `abs(i - start)` such that `nums[i] == target`. You are guaranteed that `target` exists in `nums`.

### 📌 Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^4`
- `0 <= start <= nums.length - 1`
- `target` is in `nums`

---

## 💭 Intuition
👉 Expand outward from `start` in both directions simultaneously. The first index where `nums[i] == target` gives the minimum distance.

---

## ⚡ Approach — Bidirectional Expansion from Start

### 🧠 Idea
- Iterate distance `d` from 0 to n-1.
- At each distance, check both `start - d` and `start + d` (if within bounds).
- Return `d` as soon as we find the target at either position.

---

## 💻 Code

```python
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)

        for d in range(n):
            if start - d >= 0 and nums[start - d] == target:
                return d
            if start + d < n and nums[start + d] == target:
                return d
```

---

## 🧠 Dry Run
### Input
```
nums = [1,2,3,4,5], target = 5, start = 3
```
### Steps
```
d=0: check nums[3]=4 ≠ 5, check nums[3]=4 ≠ 5
d=1: check nums[2]=3 ≠ 5, check nums[4]=5 == 5 → return 1
```

---

## ⏱️ Time Complexity
```
O(n), where n is the length of nums
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- Target is at the start index itself → returns 0
- Target only exists at one end of the array
- Multiple occurrences of target — we naturally find the closest first

---

## 🎯 Interview Takeaways
- Expanding outward from a center point is a clean way to find the nearest match.
- This avoids sorting and preserves index information.

---

## 📌 Key Pattern
👉 **"Bidirectional expansion from a center point to find the nearest match"**

---

## 🔁 Related Problems
- 744. Find Smallest Letter Greater Than Target
- 658. Find K Closest Elements
- 2089. Find Target Indices After Sorting Array

---

## 🚀 Final Thoughts
The bidirectional expansion approach is elegant because it guarantees the first match found is the closest. This is more efficient than scanning the entire array and tracking minimums.

---

✨ **Rule to remember:**
> To find the nearest occurrence, expand outward from the starting point — the first hit is the answer.
