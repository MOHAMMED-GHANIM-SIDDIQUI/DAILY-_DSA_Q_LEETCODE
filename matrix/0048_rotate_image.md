# 48. Rotate Image

## 🔗 Problem Link
https://leetcode.com/problems/rotate-image/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Math, Matrix

---

## 🧩 Problem Summary
You are given an `n x n` 2D matrix representing an image. Rotate the image by 90 degrees (clockwise). You have to rotate the image in-place — modify the input 2D matrix directly. Do **not** allocate another 2D matrix and do the rotation.

### 📌 Constraints
- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

---

## 💭 Intuition
👉 A 90° clockwise rotation can be decomposed into two simple in-place steps:
1. **Transpose** the matrix (swap across the main diagonal) — rows become columns.
2. **Reverse each row** — flips horizontally to complete the clockwise rotation.

This avoids allocating an auxiliary matrix and uses only O(1) extra space.

---

## ⚡ Approach — Transpose + Reverse Rows

### 🧠 Idea
- Walk the upper triangle (`j > i`) and swap `matrix[i][j]` with `matrix[j][i]` to transpose in place.
- Reverse each row using slicing `matrix[i] = matrix[i][::-1]`.
- Combined effect = 90° clockwise rotation.

---

## 💻 Code

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse each row
        for i in range(n):
            matrix[i] = matrix[i][::-1]
```

---

## 🧠 Dry Run
### Input
```
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
```
### Steps
```
Transpose (swap across main diagonal):
  [[1,4,7],
   [2,5,8],
   [3,6,9]]

Reverse each row:
  [[7,4,1],
   [8,5,2],
   [9,6,3]]

Final = 90° clockwise rotation ✅
```

---

## ⏱️ Time Complexity
```
O(n^2) — every cell is visited a constant number of times
```

## 💾 Space Complexity
```
O(1) — rotation is performed in-place (row reversal via slicing creates a new row of size n,
       but no auxiliary 2D matrix is allocated)
```

---

## ⚠️ Edge Cases
- `n == 1` → single cell, already rotated (no-op)
- `n == 2` → smallest non-trivial case; transpose + reverse still works
- Duplicate values → swaps are still correct
- Negative values → no impact, only positions change

---

## 🎯 Interview Takeaways
- 90° clockwise = **transpose + reverse rows**.
- 90° counter-clockwise = **transpose + reverse columns** (or reverse rows then transpose).
- 180° = reverse rows + reverse columns (or apply 90° twice).
- Always iterate the upper triangle (`j > i`) when transposing in place — iterating the full grid swaps each pair twice and undoes the transpose.

---

## 📌 Key Pattern
👉 **"In-place 90° clockwise rotation = transpose + reverse each row"**

---

## 🔁 Related Problems
- 1886. Determine Whether Matrix Can Be Obtained By Rotation
- 867. Transpose Matrix
- 54. Spiral Matrix
- 73. Set Matrix Zeroes

---

## 🚀 Final Thoughts
Classic in-place matrix manipulation problem. The transpose-then-reverse trick is one of those patterns that, once seen, becomes a permanent tool — every rotation variant is a small twist on it.

---

✨ **Rule to remember:**
> 90° clockwise rotation in-place = transpose across the main diagonal, then reverse each row.
