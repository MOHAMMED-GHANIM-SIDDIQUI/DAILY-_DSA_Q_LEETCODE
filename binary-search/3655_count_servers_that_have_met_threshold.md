# 3655. Count Servers That Have Met Threshold

## 🔗 Problem Link
https://leetcode.com/problems/count-servers-that-have-met-threshold/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Binary Search, Dynamic Programming, Greedy, Sorting

---

## 🧩 Problem Summary
Given robots at positions with firing distances, and walls at various positions, each robot can fire either left or right (but not both). Robots cannot overlap their firing ranges. Maximize the total number of walls destroyed by all robots combined.

### 📌 Constraints
- `1 <= robots.length <= 10^5`
- `1 <= walls.length <= 10^5`
- Positions and distances are positive integers

---

## 💭 Intuition
👉 Sort robots and walls by position. For each robot, compute how many walls it can hit firing left vs right. Use DP with two states (previous robot fired left or right) to maximize total walls destroyed without range overlap.

---

## ⚡ Approach — Sorted DP with Binary Search

### 🧠 Idea
- Sort robots by position and walls by position.
- For each robot, compute firing range `[L, R]` constrained by neighboring robots.
- Use binary search (`bisect`) to count walls in any range.
- DP: `solve(i, prevDir)` returns max walls from robot `i` onward, given the previous robot's direction. If previous fired right, current's left range is constrained.

---

## 💻 Code

```python
from bisect import bisect_left, bisect_right

class Solution:
    def maxWalls(self, robots, distance, walls):
        n = len(robots)

        # combine robot position and distance
        roboDist = [(robots[i], distance[i]) for i in range(n)]
        roboDist.sort()
        walls.sort()

        # helper: count walls in [l, r]
        def countWalls(l, r):
            left = bisect_left(walls, l)
            right = bisect_right(walls, r)
            return right - left

        # build range array
        range_ = []
        for i in range(n):
            pos, d = roboDist[i]

            leftLimit  = 1 if i == 0 else roboDist[i-1][0] + 1
            rightLimit = int(1e9) if i == n-1 else roboDist[i+1][0] - 1

            L = max(pos - d, leftLimit)
            R = min(pos + d, rightLimit)

            range_.append((L, R))

        # DP table
        t = [[-1]*2 for _ in range(n+1)]

        def solve(i, prevDir):
            if i == n:
                return 0

            if t[i][prevDir] != -1:
                return t[i][prevDir]

            leftStart = range_[i][0]

            if prevDir == 1:  # previous fired right
                leftStart = max(leftStart, range_[i-1][1] + 1)

            # fire left
            leftTake = countWalls(leftStart, roboDist[i][0]) + solve(i+1, 0)

            # fire right
            rightTake = countWalls(roboDist[i][0], range_[i][1]) + solve(i+1, 1)

            t[i][prevDir] = max(leftTake, rightTake)
            return t[i][prevDir]

        return solve(0, 0)
```

---

## 🧠 Dry Run
### Input
```
robots = [2, 5], distance = [3, 2], walls = [1, 3, 4, 6]
```
### Steps
```
roboDist sorted: [(2,3), (5,2)]
walls sorted: [1, 3, 4, 6]

Range computation:
  Robot 0 (pos=2, d=3): L=max(-1,1)=1, R=min(5,4)=4 → [1,4]
  Robot 1 (pos=5, d=2): L=max(3,3)=3, R=min(7,1e9)=7 → [3,7]

solve(0, 0):
  Fire left: walls in [1,2] = {1} = 1, + solve(1, 0)
    solve(1, 0): fire left [3,5]=2 walls, fire right [5,7]=1 wall → max=2
  leftTake = 1 + 2 = 3

  Fire right: walls in [2,4] = {3,4} = 2, + solve(1, 1)
    solve(1, 1): leftStart = max(3, 5) = 5, fire left [5,5]=0, fire right [5,7]=1 → max=1
  rightTake = 2 + 1 = 3

Result: 3
```

---

## ⏱️ Time Complexity
```
O(n log n + m log m) — sorting + O(n) DP states with O(log m) binary search each
```

## 💾 Space Complexity
```
O(n + m) — for ranges, DP table, and sorted arrays
```

---

## ⚠️ Edge Cases
- Single robot → fire in direction with more walls
- No walls → return 0
- Robots at same position (shouldn't happen per constraints)
- Robot range doesn't reach any wall

---

## 🎯 Interview Takeaways
- Sorting both robots and walls enables efficient range queries via binary search.
- DP with "previous direction" state handles the non-overlap constraint cleanly.
- `bisect_left` and `bisect_right` together count elements in a range.

---

## 📌 Key Pattern
👉 **"Sort + Binary Search for counting, DP with direction state for non-overlapping range selection."**

---

## 🔁 Related Problems
- 435. Non-overlapping Intervals
- 452. Minimum Number of Arrows to Burst Balloons
- 1235. Maximum Profit in Job Scheduling

---

## 🚀 Final Thoughts
This problem combines sorting, binary search, and DP beautifully. The key insight is that the direction choice of one robot affects the next robot's available range, making it a natural DP problem with a binary state.

---

✨ **Rule to remember:**
> "When choices at one step constrain the next, use DP with state tracking the previous decision."
