# 1266. Minimum Time Visiting All Points

## 🔗 Problem Link
https://leetcode.com/problems/minimum-time-visiting-all-points/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Math, Geometry

---

## 🧩 Problem Summary

Given an array of points on a 2D plane, return the minimum time in seconds to visit all points in order. You can move one unit in any of 8 directions (including diagonals) per second.

### 📌 Constraints
- `points.length >= 1`
- `points[i].length == 2`
- `-1000 <= points[i][0], points[i][1] <= 1000`

---

## 💭 Intuition

👉 With 8-directional movement (including diagonals), the minimum time to travel between two points is the Chebyshev distance: `max(|dx|, |dy|)`. Diagonal moves cover both x and y simultaneously.

---

## ⚡ Approach — Chebyshev Distance Sum

### 🧠 Idea
- For each consecutive pair of points, compute `max(|x2-x1|, |y2-y1|)`.
- Sum all these distances — that's the minimum total time.

---

## 💻 Code

```python
class Solution:
  def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
    ans = 0

    for i in range(1, len(points)):
      ans += max(abs(points[i][0] - points[i - 1][0]),
                 abs(points[i][1] - points[i - 1][1]))

    return ans
```

---

## 🧠 Dry Run

### Input
```
points = [[1,1],[3,4],[-1,0]]
```

### Steps
```
From [1,1] to [3,4]:
  dx = |3-1| = 2, dy = |4-1| = 3
  time = max(2, 3) = 3

From [3,4] to [-1,0]:
  dx = |(-1)-3| = 4, dy = |0-4| = 4
  time = max(4, 4) = 4

Total = 3 + 4 = 7
```

---

## ⏱️ Time Complexity
```
O(n)
```
One pass through the points array.

---

## 💾 Space Complexity
```
O(1)
```
Only a single accumulator variable is used.

---

## ⚠️ Edge Cases
- Single point → return 0.
- Two identical consecutive points → contribute 0 to the sum.
- Points along a horizontal/vertical line → Chebyshev distance equals Manhattan distance in that direction.

---

## 🎯 Interview Takeaways
- Chebyshev distance is the correct metric for 8-directional grid movement.
- Diagonal movement lets you cover both dx and dy simultaneously.
- This problem is a direct application of a well-known distance formula.
- No need for pathfinding algorithms — the optimal path is always direct.

---

## 📌 Key Pattern
👉 **"Chebyshev distance — with diagonal moves, time = max(|dx|, |dy|)."**

---

## 🔁 Related Problems
- 1232 - Check If It Is a Straight Line
- 1030 - Matrix Cells in Distance Order
- 2013 - Detect Squares

---

## 🚀 Final Thoughts
A simple math problem once you recognize that 8-directional movement uses Chebyshev distance. The diagonal moves let you reduce the longer axis while simultaneously covering the shorter one.

---

✨ **Rule to remember:**
> "On a grid with 8-directional movement, the shortest distance between two points is max(|dx|, |dy|)."
