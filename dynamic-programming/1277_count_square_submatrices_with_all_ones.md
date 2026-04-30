# 1277. Count Square Submatrices with All Ones

## 🔗 Problem Link
https://leetcode.com/problems/count-square-submatrices-with-all-ones/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Dynamic Programming, Matrix

---

## 🧩 Problem Summary

Given an `m x n` binary matrix, return the total number of square submatrices that have all ones.

### 📌 Constraints
- `1 <= m, n <= 300`
- `matrix[i][j]` is 0 or 1.

---

## 💭 Intuition

👉 `matrix[i][j]` can represent the side length of the largest square ending at `(i, j)` as its bottom-right corner.

👉 The value at each cell also equals the count of squares ending there (a square of size k contributes squares of sizes 1, 2, ..., k).

👉 Sum all cells to get the total count.

---

## ⚡ Approach — In-Place DP

### 🧠 Idea
- For each cell `(i, j)` with value 1 (and `i > 0`, `j > 0`), update:
  `matrix[i][j] = 1 + min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])`
- This gives the largest square side length ending at `(i, j)`.
- Sum all values in the matrix — each cell's value is the number of squares it contributes.

---

## 💻 Code

```cpp
class Solution {
 public:
  int countSquares(vector<vector<int>>& matrix) {
    for (int i = 0; i < matrix.size(); ++i)
      for (int j = 0; j < matrix[0].size(); ++j)
        if (matrix[i][j] == 1 && i > 0 && j > 0)
          matrix[i][j] +=
              min({matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1]});
    return accumulate(matrix.begin(), matrix.end(), 0,
                      [](int subtotal, const vector<int>& row) {
      return subtotal + accumulate(row.begin(), row.end(), 0);
    });
  }
};
```

---

## 🧠 Dry Run

### Input
```
matrix = [[0,1,1,1],
          [1,1,1,1],
          [0,1,1,1]]
```

### Steps
```
After DP update:
  [[0,1,1,1],
   [1,1,2,2],
   [0,1,2,3]]

Sum = 0+1+1+1 + 1+1+2+2 + 0+1+2+3 = 15
Output: 15
```

---

## ⏱️ Time Complexity
```
O(m * n)
```
Each cell is visited exactly once for the DP update, and once for the summation.

---

## 💾 Space Complexity
```
O(1)
```
The matrix is modified in place — no extra space needed.

---

## ⚠️ Edge Cases
- All zeros → return 0.
- All ones → maximum possible squares.
- Single row or column → each 1 contributes exactly one 1x1 square.

---

## 🎯 Interview Takeaways
- This uses the same DP recurrence as "Maximal Square" (LeetCode 221).
- The insight that `dp[i][j]` equals the count of squares ending at `(i,j)` is key.
- In-place modification saves space but mutates the input.
- The `min` of three neighbors determines the largest possible square.

---

## 📌 Key Pattern
👉 **"Square DP — dp[i][j] = 1 + min(top, left, top-left) gives the largest square ending at (i,j), and its value is the count of squares it contributes."**

---

## 🔁 Related Problems
- 221 - Maximal Square
- 1504 - Count Submatrices With All Ones (rectangles)
- 764 - Largest Plus Sign

---

## 🚀 Final Thoughts
A beautiful DP problem where the recurrence simultaneously computes the largest square size and the count of all squares. The in-place approach makes it both time and space optimal.

---

✨ **Rule to remember:**
> "In the square DP, each cell's value is both the max square size AND the count of squares ending there."
