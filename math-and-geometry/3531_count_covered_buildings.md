# 3531. Count Covered Buildings

## 🔗 Problem Link
https://leetcode.com/problems/count-covered-buildings/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Map, Geometry

---

## 🧩 Problem Summary
Given an n x n grid and a list of building positions, count how many buildings are "covered" — meaning there exists at least one building to their north, south, east, and west on the same row/column.

### 📌 Constraints
- `1 <= n <= 10^5`
- `1 <= buildings.length <= 10^5`
- Buildings are at distinct positions on the grid

---

## 💭 Intuition
👉 A building at (x, y) is covered if there are buildings with the same x-coordinate both above and below it, AND buildings with the same y-coordinate both left and right of it. Precompute the extremes for each row and column.

---

## ⚡ Approach — Precompute Extremes per Row and Column

### 🧠 Idea
- For each column x: track the northernmost (min y) and southernmost (max y) building.
- For each row y: track the westernmost (min x) and easternmost (max x) building.
- A building at (x, y) is covered if it's strictly between all four extremes.

---

## 💻 Code

```python
class Solution:
  def countCoveredBuildings(self, n: int, buildings: list[list[int]]) -> int:
    northernmost = [math.inf] * (n + 1)
    southernmost = [0] * (n + 1)
    westernmost = [math.inf] * (n + 1)
    easternmost = [0] * (n + 1)

    for x, y in buildings:
      northernmost[x] = min(northernmost[x], y)
      southernmost[x] = max(southernmost[x], y)
      westernmost[y] = min(westernmost[y], x)
      easternmost[y] = max(easternmost[y], x)

    return sum(northernmost[x] < y < southernmost[x]
               and westernmost[y] < x < easternmost[y]
               for x, y in buildings)
```

---

## 🧠 Dry Run
### Input
```
n = 5, buildings = [[1,1],[1,3],[1,5],[3,3],[5,3]]
```
### Steps
```
Column 1: north=1, south=5
Column 3: north=3, south=3
Column 5: north=3, south=3
Row 1: west=1, east=1
Row 3: west=1, east=5
Row 5: west=1, east=1

Check each:
(1,1): north[1]=1 < 1? No → not covered
(1,3): north[1]=1 < 3 < 5=south[1]? Yes. west[3]=1 < 1? No → not covered
(1,5): south[1]=5 < 5? No → not covered
(3,3): north[3]=3 < 3? No → not covered
(5,3): north[5]=3 < 3? No → not covered

Result: 0
```

---

## ⏱️ Time Complexity
```
O(n + b) — where b is the number of buildings, one pass to compute extremes, one to count
```

## 💾 Space Complexity
```
O(n) — for the extreme value arrays
```

---

## ⚠️ Edge Cases
- Only one building per row/column → can never be covered in that direction
- All buildings in a single row → no north/south coverage
- Building at the extreme position → not covered (needs strict inequality)

---

## 🎯 Interview Takeaways
- Precomputing per-row/column extremes reduces an O(b^2) problem to O(b).
- "Covered" means strictly between extremes — use strict inequality.
- Separating the precompute phase from the query phase is a clean pattern.

---

## 📌 Key Pattern
👉 **"Precompute row/column extremes to check if an element is strictly interior."**

---

## 🔁 Related Problems
- 1274. Number of Ships in a Rectangle
- 2345. Finding the Number of Visible People in a Queue
- 807. Max Increase to Keep City Skyline

---

## 🚀 Final Thoughts
A clean geometric problem that reduces to precomputing four directional extremes. The strict inequality check ensures only truly interior buildings are counted. Elegant one-liner sum with generator expression.

---

✨ **Rule to remember:**
> To check if a point is "surrounded," precompute the min/max in each direction and verify strict inequality.
