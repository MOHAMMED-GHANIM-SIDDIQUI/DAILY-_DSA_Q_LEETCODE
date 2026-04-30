# 2975. Maximum Square Area by Removing Fences From a Field

## 🔗 Problem Link
https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Set, Sorting, Enumeration

---

## 🧩 Problem Summary
Given a field of size `m x n` with horizontal fences at `hFences` and vertical fences at `vFences`, remove some fences to create the largest possible square. The square sides must align with existing fence positions (including boundaries 1 and m/n). Return the maximum square area modulo 10^9 + 7, or -1 if no square is possible.

### 📌 Constraints
- `3 <= m, n <= 10^9`
- `1 <= hFences.length, vFences.length <= 600`
- `2 <= hFences[i] <= m - 1`
- `2 <= vFences[i] <= n - 1`

---

## 💭 Intuition
👉 Enumerate all possible gap sizes (distances between any two fence positions) for both horizontal and vertical fences. The largest gap that appears in both sets gives the maximum square side length.

---

## ⚡ Approach — Gap Set Intersection

### 🧠 Idea
- Add boundaries (1 and m for horizontal, 1 and n for vertical) to the fence arrays.
- Sort both arrays.
- Compute all pairwise differences for horizontal fences → `hGaps` set.
- Compute all pairwise differences for vertical fences → `vGaps` set.
- Find the largest value present in both sets.
- Return that value squared mod 10^9+7, or -1 if no common gap exists.

---

## 💻 Code

```python
class Solution:
  def maximizeSquareArea(
      self,
      m: int,
      n: int,
      hFences: list[int],
      vFences: list[int],
  ) -> int:
    hFences = sorted(hFences + [1, m])
    vFences = sorted(vFences + [1, n])
    hGaps = {hFences[i] - hFences[j]
             for i in range(len(hFences))
             for j in range(i)}
    vGaps = {vFences[i] - vFences[j]
             for i in range(len(vFences))
             for j in range(i)}
    maxGap = next((hGap
                  for hGap in sorted(hGaps, reverse=True)
                  if hGap in vGaps), -1)
    return -1 if maxGap == -1 else maxGap**2 % (10**9 + 7)
```

---

## 🧠 Dry Run
### Input
```
m = 4, n = 3, hFences = [2,3], vFences = [2]
```
### Steps
```
hFences = sorted([2,3,1,4]) = [1,2,3,4]
vFences = sorted([2,1,3]) = [1,2,3]

hGaps = {2-1=1, 3-1=2, 3-2=1, 4-1=3, 4-2=2, 4-3=1} = {1,2,3}
vGaps = {2-1=1, 3-1=2, 3-2=1} = {1,2}

sorted(hGaps, reverse=True) = [3,2,1]
3 in vGaps? No
2 in vGaps? Yes → maxGap = 2

Result: 2^2 % (10^9+7) = 4
```

---

## ⏱️ Time Complexity
```
O(h^2 + v^2 + h^2 log(h^2)) where h = len(hFences), v = len(vFences).
Pairwise differences: O(h^2 + v^2). Sorting gaps: O(h^2 log h).
```

## 💾 Space Complexity
```
O(h^2 + v^2) — for the gap sets.
```

---

## ⚠️ Edge Cases
- No common gap exists: return -1.
- Only boundaries exist (no internal fences): the only gap is m-1 and n-1.
- Very large m, n values: gaps can be large but we only store O(h^2) of them.

---

## 🎯 Interview Takeaways
- Enumerating all pairwise differences and using set intersection is a powerful technique.
- Adding boundaries to the fence arrays simplifies edge handling.
- Sorting in descending order and taking the first match gives the maximum efficiently.

---

## 📌 Key Pattern
👉 **"Enumerate all pairwise gaps, intersect the two sets, take the maximum common value."**

---

## 🔁 Related Problems
- 2943. Maximize Area of Square Hole in Grid
- 1. Two Sum (pairwise difference concept)
- 2975. Maximum Square Area by Removing Fences From a Field

---

## 🚀 Final Thoughts
This problem is an elegant application of set-based enumeration. By computing all possible distances between fence positions in each dimension and finding the largest common distance, we avoid brute-forcing grid positions entirely. The modular arithmetic at the end is a small but important detail.

---

✨ **Rule to remember:**
> "Enumerate gaps in each dimension, intersect, and take the max — that's your square side."
