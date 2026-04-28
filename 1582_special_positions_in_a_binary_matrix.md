# 1582. Special Positions in a Binary Matrix

## 🔗 Problem Link
https://leetcode.com/problems/special-positions-in-a-binary-matrix/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Matrix

---

## 🧩 Problem Summary
Given an `m x n` binary matrix `mat`, return the number of special positions in the matrix. A position `(i, j)` is special if `mat[i][j] == 1` and all other elements in row `i` and column `j` are `0`.

### 📌 Constraints
- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 100`
- `mat[i][j]` is `0` or `1`

---

## 💭 Intuition
👉 A cell is "special" only when it is the sole `1` in its entire row AND its entire column. Precomputing row sums and column sums lets us verify this in O(1) per cell.

---

## ⚡ Approach — Row/Column Sum Precomputation

### 🧠 Idea
- Compute the sum of each row and each column.
- Iterate through every cell; if `grid[i][j] == 1` and `row_sum[i] == 1` and `col_sum[j] == 1`, it is special.

---

## 💻 Code

```python
class Solution:
    def numSpecial(self, grid: List[List[int]]) -> int:

        row_sum_LC = [sum(row) for row in grid]

        col_sum_LC = [sum(col) for col in (zip(*grid))]
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and row_sum_LC[i] == 1 and col_sum_LC[j] == 1:
                    ans +=1
        return ans
```

---

## 🧠 Dry Run
### Input
```
mat = [[1,0,0],[0,0,1],[1,0,0]]
```
### Steps
```
row_sum = [1, 1, 1]
col_sum = [2, 0, 1]

(0,0): grid=1, row_sum=1, col_sum=2 → NOT special
(1,2): grid=1, row_sum=1, col_sum=1 → SPECIAL → ans=1
(2,0): grid=1, row_sum=1, col_sum=2 → NOT special

Result: 1
```

---

## ⏱️ Time Complexity
```
O(m * n) — one pass to compute sums, one pass to check each cell
```

## 💾 Space Complexity
```
O(m + n) — for storing row and column sums
```

---

## ⚠️ Edge Cases
- Matrix with all zeros → answer is 0.
- Matrix with a single cell `[[1]]` → answer is 1.
- Every row/column has more than one `1` → answer is 0.

---

## 🎯 Interview Takeaways
- Precomputing row and column aggregates is a standard technique for matrix problems.
- Using `zip(*grid)` in Python elegantly transposes rows into columns.

---

## 📌 Key Pattern
👉 **"Precompute row/column sums, then verify per-cell conditions in O(1)"**

---

## 🔁 Related Problems
- 48. Rotate Image
- 73. Set Matrix Zeroes
- 2482. Difference Between Ones and Zeros in Row and Column

---

## 🚀 Final Thoughts
A clean easy-level problem that reinforces the row/column precomputation pattern. The key observation is that "special" boils down to both sums being exactly 1.

---

✨ **Rule to remember:**
> If a cell must be the only `1` in its row and column, just check that both the row sum and column sum equal 1.
