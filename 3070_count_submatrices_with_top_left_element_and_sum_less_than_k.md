# 3070. Count Submatrices with Top-Left Element and Sum Less Than k

## 🔗 Problem Link
https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Matrix, Prefix Sum

---

## 🧩 Problem Summary
Given a 2D integer matrix `grid` and an integer `k`, count the number of submatrices that have their top-left corner at `(0, 0)` and whose element sum is less than or equal to `k`.

### 📌 Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= n, m <= 1000`
- `0 <= grid[i][j] <= 1000`
- `1 <= k <= 10^9`

---

## 💭 Intuition
👉 Since all submatrices must start at `(0, 0)`, each submatrix is uniquely defined by its bottom-right corner `(i, j)`. We can use a 2D prefix sum to compute each submatrix sum in O(1) and count those that are <= k.

---

## ⚡ Approach — 2D Prefix Sum

### 🧠 Idea
- Build a 2D prefix sum array where `prefix[i+1][j+1]` = sum of `grid[0..i][0..j]`.
- For each cell `(i, j)`, check if the prefix sum is <= k.
- Count all valid submatrices.

---

## 💻 Code

```python
class Solution:
  def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
    m = len(grid)
    n = len(grid[0])
    ans = 0
    # prefix[i][j] := the sum of matrix[0..i)[0..j)
    prefix = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
      for j in range(n):
        prefix[i + 1][j + 1] = (grid[i][j] + prefix[i][j + 1] +
                                prefix[i + 1][j] - prefix[i][j])
        if prefix[i + 1][j + 1] <= k:
          ans += 1

    return ans
```

---

## 🧠 Dry Run
### Input
```
grid = [[7,6,3],[6,6,1]], k = 18
```
### Steps
```
1. prefix[1][1] = 7 <= 18 => ans = 1
2. prefix[1][2] = 7+6 = 13 <= 18 => ans = 2
3. prefix[1][3] = 7+6+3 = 16 <= 18 => ans = 3
4. prefix[2][1] = 7+6 = 13 <= 18 => ans = 4
5. prefix[2][2] = 7+6+6+6 = 25 > 18 => skip
6. prefix[2][3] = 7+6+3+6+6+1 = 29 > 18 => skip
Result: 4
```

---

## ⏱️ Time Complexity
```
O(m * n) — single pass to build prefix sums and count.
```

## 💾 Space Complexity
```
O(m * n) for the prefix sum array.
```

---

## ⚠️ Edge Cases
- All elements are 0: every submatrix has sum 0, answer is m * n.
- `k` is very large: all submatrices qualify, answer is m * n.
- `grid[0][0] > k`: answer is 0.

---

## 🎯 Interview Takeaways
- When the top-left is fixed at (0,0), the prefix sum directly gives each submatrix sum.
- The inclusion-exclusion formula for 2D prefix sums: `prefix[i+1][j+1] = grid[i][j] + prefix[i][j+1] + prefix[i+1][j] - prefix[i][j]`.
- Counting and computing simultaneously saves an extra pass.

---

## 📌 Key Pattern
👉 **"2D prefix sum for fixed-origin submatrix sum queries"**

---

## 🔁 Related Problems
- 304. Range Sum Query 2D - Immutable
- 1314. Matrix Block Sum
- 363. Max Sum of Rectangle No Larger Than K

---

## 🚀 Final Thoughts
A clean application of 2D prefix sums. The fixed top-left corner simplifies the problem significantly since we only need to iterate over bottom-right corners and check one prefix sum value per submatrix.

---

✨ **Rule to remember:**
> When submatrices share a fixed corner, 2D prefix sums give each submatrix sum in O(1) — just iterate over the opposite corner.
