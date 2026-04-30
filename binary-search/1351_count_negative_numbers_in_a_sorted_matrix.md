# 1351. Count Negative Numbers in a Sorted Matrix

## 🔗 Problem Link
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Binary Search, Matrix

---

## 🧩 Problem Summary
Given an `m x n` matrix `grid` where each row and column is sorted in non-increasing order, count the number of negative numbers in the matrix.

### 📌 Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100`
- `-100 <= grid[i][j] <= 100`

---

## 💭 Intuition
👉 Since rows are sorted in non-increasing order, once we find a negative number in a row, everything to its right is also negative. Starting from the bottom-left corner, we can walk a staircase path in O(m + n) time.

---

## ⚡ Approach — Staircase / Bottom-Left Traversal

### 🧠 Idea
- Start at bottom-left corner `(m-1, 0)`.
- If the current cell is negative, all cells to the right in that row are also negative → add `n - j` to the count and move up.
- If the current cell is non-negative, move right.
- Continue until out of bounds.

---

## 💻 Code

```python
class Solution:
  def countNegatives(self, grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    ans = 0
    i = m - 1
    j = 0

    while i >= 0 and j < n:
      if grid[i][j] < 0:
        ans += n - j
        i -= 1
      else:
        j += 1

    return ans
```

---

## 🧠 Dry Run
### Input
```
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
```
### Steps
```
Start: i=3, j=0
grid[3][0] = -1 < 0 → ans += 4-0 = 4, i=2
grid[2][0] = 1 >= 0 → j=1
grid[2][1] = 1 >= 0 → j=2
grid[2][2] = -1 < 0 → ans += 4-2 = 2, i=1
grid[1][2] = 1 >= 0 → j=3
grid[1][3] = -1 < 0 → ans += 4-3 = 1, i=0
grid[0][3] = -1 < 0 → ans += 4-3 = 1, i=-1
Total ans = 4+2+1+1 = 8
```

---

## ⏱️ Time Complexity
```
O(m + n)
```

## 💾 Space Complexity
```
O(1)
```

---

## ⚠️ Edge Cases
- All elements are negative → count = m * n
- All elements are non-negative → count = 0
- Single row or single column matrix

---

## 🎯 Interview Takeaways
- The staircase traversal exploits the sorted property in both dimensions.
- This is better than binary search per row (O(m log n)) for this problem.
- Bottom-left or top-right are canonical starting points for sorted matrix traversal.

---

## 📌 Key Pattern
👉 **"Staircase traversal on a sorted matrix — start from bottom-left or top-right."**

---

## 🔁 Related Problems
- 240. Search a 2D Matrix II
- 74. Search a 2D Matrix

---

## 🚀 Final Thoughts
An elegant O(m + n) approach that leverages the sorted structure of the matrix. The staircase technique is a must-know pattern for sorted 2D grids.

---

✨ **Rule to remember:**
> In a sorted matrix, start from a corner where one direction increases and the other decreases.
