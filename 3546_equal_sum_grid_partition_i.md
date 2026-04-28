# 3546. Equal Sum Grid Partition I

## 🔗 Problem Link
https://leetcode.com/problems/equal-sum-grid-partition-i/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Matrix, Prefix Sum

---

## 🧩 Problem Summary
Given a 2D grid of integers, determine if it's possible to make a single horizontal or vertical cut that divides the grid into two parts with equal sums. Return `true` if such a cut exists, `false` otherwise.

### 📌 Constraints
- `1 <= m, n <= 10^5`
- `m * n <= 10^5`
- `1 <= grid[i][j] <= 10^9`

---

## 💭 Intuition
👉 Compute row sums and column sums, then check if any prefix of row sums or column sums equals exactly half the total — if the total is odd, no valid cut exists.

---

## ⚡ Approach — Prefix Sum on Rows and Columns

### 🧠 Idea
- Compute total sum; if odd, return False.
- Compute cumulative row sums; if any prefix equals half the total, a horizontal cut works.
- Compute cumulative column sums; if any prefix equals half the total, a vertical cut works.

---

## 💻 Code

```python
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
      m , n = len(grid) , len(grid[0])
      row_sum = list(map(lambda row: sum(row),grid))
      col_sum = list(map(lambda col: sum(col),zip(*grid)))
      total_sum = sum(row_sum)
      if total_sum % 2 != 0:
        return False
      else:
        target = total_sum // 2
        cum_sum = 0
        for val in row_sum:
          cum_sum +=val
          if cum_sum == target:
            return True
        cum_sum = 0
        for val in col_sum:
          cum_sum +=val
          if cum_sum == target:
            return True
      return False
```

---

## 🧠 Dry Run
### Input
```
grid = [[1, 2, 3],
        [4, 5, 6]]
```
### Steps
```
row_sum = [6, 15]  → total = 21 → odd → return False

grid = [[1, 3],
        [2, 4]]
row_sum = [4, 6], col_sum = [3, 7], total = 10, target = 5
  Row prefix: 4 ≠ 5, 10 ≠ 5
  Col prefix: 3 ≠ 5, 10 ≠ 5
  → return False

grid = [[1, 1],
        [1, 1]]
row_sum = [2, 2], total = 4, target = 2
  Row prefix: 2 == 2 → return True
```

---

## ⏱️ Time Complexity
```
O(m * n) — to compute row sums and column sums
```

## 💾 Space Complexity
```
O(m + n) — for storing row and column sums
```

---

## ⚠️ Edge Cases
- Odd total sum → impossible
- Single row or single column grid
- All elements are the same
- Very large values (check overflow in languages without arbitrary precision)

---

## 🎯 Interview Takeaways
- Always check parity of total before attempting partition.
- `zip(*grid)` is a Pythonic way to transpose a matrix for column operations.
- Prefix sum is the go-to technique for partition problems.

---

## 📌 Key Pattern
👉 **"Prefix sum on rows and columns — check if any cut point yields exactly half the total."**

---

## 🔁 Related Problems
- 3548. Equal Sum Grid Partition II
- 416. Partition Equal Subset Sum
- 1013. Partition Array Into Three Parts With Equal Sum

---

## 🚀 Final Thoughts
A clean prefix sum problem. The key is recognizing that a single straight cut (horizontal or vertical) means we only need to check cumulative row sums and column sums against half the total.

---

✨ **Rule to remember:**
> "For grid partition with a single cut, reduce to 1D prefix sums on rows and columns."
