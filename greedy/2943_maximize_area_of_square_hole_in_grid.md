# 2943. Maximize Area of Square Hole in Grid

## 🔗 Problem Link
https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Sorting, Greedy

---

## 🧩 Problem Summary
Given a grid with horizontal and vertical bars, some bars can be removed (given in `hBars` and `vBars`). Find the maximum area of a square hole that can be created by removing bars. The hole must be formed by consecutive removed bars.

### 📌 Constraints
- `2 <= n, m <= 10^9`
- `1 <= hBars.length, vBars.length <= 10^3`
- `2 <= hBars[i] <= n`
- `2 <= vBars[i] <= m`
- All values in `hBars` and `vBars` are distinct.

---

## 💭 Intuition
👉 The maximum square hole is limited by the minimum of the maximum consecutive gap in horizontal bars and vertical bars. Find the longest run of consecutive bars in each direction — that run plus the surrounding fixed bars gives the gap size. The square side is the minimum of the two gaps.

---

## ⚡ Approach — Longest Consecutive Run in Sorted Bars

### 🧠 Idea
- Sort each bar array.
- Find the longest run of consecutive values (bars differing by 1).
- A run of length `k` creates a gap of size `k + 1` (including the fixed bars on each side).
- The square side = min(horizontal gap, vertical gap), area = side^2.

---

## 💻 Code

```python
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        gap = min(self.maxContinousGap(hBars), self.maxContinousGap(vBars))
        return gap * gap

    def maxContinousGap(self, bars: List[int]) -> int:
        if not bars:
            return 1  # no bars removed → no hole bigger than 1

        bars.sort()
        res = 2
        runningGap = 2

        for i in range(1, len(bars)):
            if bars[i] == bars[i - 1] + 1:
                runningGap += 1
            else:
                runningGap = 2
            res = max(res, runningGap)

        return res
```

---

## 🧠 Dry Run
### Input
```
n = 2, m = 1, hBars = [2,3], vBars = [2]
```
### Steps
```
hBars sorted: [2,3]
  i=1: bars[1]=3 == bars[0]+1=3 → runningGap=3, res=3
  maxContinousGap(hBars) = 3

vBars sorted: [2]
  Single element → res=2
  maxContinousGap(vBars) = 2

gap = min(3, 2) = 2
area = 2 * 2 = 4
```

---

## ⏱️ Time Complexity
```
O(h log h + v log v) where h and v are the lengths of hBars and vBars. Sorting dominates.
```

## 💾 Space Complexity
```
O(1) — sorting in-place, constant extra variables.
```

---

## ⚠️ Edge Cases
- No bars to remove in one direction: gap is 1, area is 1.
- All bars consecutive in both directions: maximum possible hole.
- Single bar in each direction: gap is 2, area is 4.

---

## 🎯 Interview Takeaways
- Consecutive run detection after sorting is a fundamental technique.
- The square constraint means taking the minimum of two independent maximums.
- The "+1" offset (run of k bars → gap of k+1) accounts for the fixed boundary bars.

---

## 📌 Key Pattern
👉 **"Longest consecutive run determines the maximum gap; square side = min of two gaps."**

---

## 🔁 Related Problems
- 128. Longest Consecutive Sequence
- 2975. Maximum Square Area by Removing Fences From a Field
- 2943. Maximize Area of Square Hole in Grid

---

## 🚀 Final Thoughts
The problem reduces to finding the longest consecutive subsequence in two sorted arrays. The square constraint introduces the min operation. A clean and efficient solution that combines sorting with a single-pass consecutive run detection.

---

✨ **Rule to remember:**
> "Consecutive bars removed = gap size; square hole = min gap across both dimensions."
