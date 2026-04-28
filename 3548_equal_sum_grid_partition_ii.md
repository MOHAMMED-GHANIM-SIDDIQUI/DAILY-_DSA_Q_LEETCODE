# 3548. Equal Sum Grid Partition II

## 🔗 Problem Link
https://leetcode.com/problems/equal-sum-grid-partition-ii/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Matrix, Prefix Sum, Greedy, Enumeration

---

## 🧩 Problem Summary
Given a 2D grid, determine if you can make a single horizontal or vertical cut and optionally move at most one element from one side to the other (changing its value to 0) so that both halves have equal sums. The element moved must be on the border of the cut.

### 📌 Constraints
- `1 <= m, n <= 10^5`
- `m * n <= 10^5`
- `1 <= grid[i][j] <= 10^9`

---

## 💭 Intuition
👉 Try every possible cut in all 4 directions (top-down, bottom-up, left-right, right-left). For each cut position, the difference `topSum - botSum` must either be 0 or match a border element that can be "moved" — track seen border elements to check efficiently.

---

## ⚡ Approach — Enumerate Cuts with Border Element Matching

### 🧠 Idea
- For each direction (rows forward/backward, columns forward/backward), compute prefix sums.
- At each cut, compute the difference between the two halves.
- Check if the difference is 0 (direct partition) or if the difference equals a specific corner/border value that can be transferred.
- Use a set to track elements seen so far for multi-element border checks.

---

## 💻 Code

```python
class Solution:
  def canPartitionGrid(self, grid: list[list[int]]) -> bool:
    summ = sum(map(sum, grid))
    def canPartition(grid: list[list[int]]) -> bool:
      topSum = 0
      seen = set()
      for i, row in enumerate(grid):
        topSum += sum(row)
        botSum = summ - topSum
        seen |= set(row)
        if topSum - botSum in (0, grid[0][0],  grid[0][-1], row[0]):
          return True
        if len(grid[0]) > 1 and i > 0 and topSum - botSum in seen:
          return True
      return False

    return (canPartition(grid) or
            canPartition(grid[::-1]) or
            canPartition(list(zip(*grid))[::-1]) or
            canPartition(list(zip(*grid))))
```

---

## 🧠 Dry Run
### Input
```
grid = [[1, 2],
        [3, 4]]
```
### Steps
```
summ = 10

canPartition(grid) — rows top-to-bottom:
  i=0, row=[1,2]: topSum=3, botSum=7, diff=-4
    Check -4 in (0, 1, 2, 1) → No
  i=1, row=[3,4]: topSum=10, botSum=0, diff=10
    last row so no valid cut → False

canPartition(grid[::-1]) — rows bottom-to-top:
  i=0, row=[3,4]: topSum=7, botSum=3, diff=4
    Check 4 in (0, 3, 4, 3) → Yes (4 matches grid[0][-1])
    → return True

Result: True
```

---

## ⏱️ Time Complexity
```
O(m * n) — scanning all elements for each of 4 directions
```

## 💾 Space Complexity
```
O(m * n) — for the seen set and transposed grid
```

---

## ⚠️ Edge Cases
- Difference is exactly 0 → no element needs to be moved
- Only one row or one column
- The element to move is at a corner (appears in multiple checks)
- Grid with a single cell

---

## 🎯 Interview Takeaways
- Checking all 4 orientations avoids complex case analysis.
- The `seen` set elegantly handles "can we find a border element matching the difference."
- Reducing the problem to "does difference match a movable element" is the key insight.

---

## 📌 Key Pattern
👉 **"Try all orientations, check if the partition difference matches a border element that can be transferred."**

---

## 🔁 Related Problems
- 3546. Equal Sum Grid Partition I
- 416. Partition Equal Subset Sum
- 1049. Last Stone Weight II

---

## 🚀 Final Thoughts
This problem extends the basic grid partition by allowing one element transfer. The clever trick of trying all 4 orientations and checking if the difference matches a border element keeps the solution clean and avoids messy case handling.

---

✨ **Rule to remember:**
> "When a partition is almost equal, check if transferring a single border element bridges the gap."
