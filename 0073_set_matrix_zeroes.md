# 73. Set Matrix Zeroes

## 🔗 Problem Link
https://leetcode.com/problems/set-matrix-zeroes/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, Matrix

---

## 🧩 Problem Summary
Given an m x n integer matrix, if an element is 0, set its entire row and column to 0. You must do it in-place.

### 📌 Constraints
- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-2^31 <= matrix[i][j] <= 2^31 - 1`

---

## 💭 Intuition
👉 Use the first row and first column of the matrix itself as markers to record which rows and columns should be zeroed, achieving O(1) extra space.

---

## ⚡ Approach — In-Place Markers with First Row/Column

### 🧠 Idea
- First, check if the first row or first column originally contains any zeros (store in boolean flags).
- Use the rest of the matrix to mark zeros: if `matrix[i][j] == 0`, set `matrix[i][0] = 0` and `matrix[0][j] = 0`.
- Iterate through the inner matrix (excluding first row/column) and zero out cells based on markers.
- Finally, zero out the first row and first column if needed based on the saved flags.

---

## 💻 Code

```cpp
class Solution {
 public:
  void setZeroes(vector<vector<int>>& matrix) {
    const int m = matrix.size();
    const int n = matrix[0].size();
    bool shouldFillFirstRow = false;
    bool shouldFillFirstCol = false;

    for (int j = 0; j < n; ++j)
      if (matrix[0][j] == 0) {
        shouldFillFirstRow = true;
        break;
      }

    for (int i = 0; i < m; ++i)
      if (matrix[i][0] == 0) {
        shouldFillFirstCol = true;
        break;
      }

    // Store the information in the first row and the first column.
    for (int i = 1; i < m; ++i)
      for (int j = 1; j < n; ++j)
        if (matrix[i][j] == 0) {
          matrix[i][0] = 0;
          matrix[0][j] = 0;
        }

    // Fill 0s for the matrix except the first row and the first column.
    for (int i = 1; i < m; ++i)
      for (int j = 1; j < n; ++j)
        if (matrix[i][0] == 0 || matrix[0][j] == 0)
          matrix[i][j] = 0;

    // Fill 0s for the first row if needed.
    if (shouldFillFirstRow)
      for (int j = 0; j < n; ++j)
        matrix[0][j] = 0;

    // Fill 0s for the first column if needed.
    if (shouldFillFirstCol)
      for (int i = 0; i < m; ++i)
        matrix[i][0] = 0;
  }
};
```

---

## 🧠 Dry Run
### Input
```
matrix = [[1,1,1],
          [1,0,1],
          [1,1,1]]
```
### Steps
```
Step 1: shouldFillFirstRow = false, shouldFillFirstCol = false
Step 2: matrix[1][1]==0 -> set matrix[1][0]=0, matrix[0][1]=0
        matrix = [[1,0,1],[0,0,1],[1,1,1]]
Step 3: Fill inner matrix based on markers:
        matrix[1][1]=0 (row marker), matrix[1][2]=0 (row marker)
        matrix[2][1]=0 (col marker)
        matrix = [[1,0,1],[0,0,0],[1,0,1]]
Step 4: First row/col flags are false, no change.
Result: [[1,0,1],[0,0,0],[1,0,1]]
```

---

## ⏱️ Time Complexity
```
O(m * n)
```

## 💾 Space Complexity
```
O(1) — only two boolean variables used as extra space
```

---

## ⚠️ Edge Cases
- Matrix with no zeros — no changes needed.
- Entire matrix is zeros — everything stays zero.
- Zero in the first row/column — handled by boolean flags.
- Single row or single column matrix.

---

## 🎯 Interview Takeaways
- Using the matrix itself as storage is a common O(1) space trick.
- Order of operations matters: mark first, then fill, then handle first row/column last.
- Always consider edge cases with boundary rows/columns.

---

## 📌 Key Pattern
👉 **"Use the first row and column as in-place markers to avoid extra space"**

---

## 🔁 Related Problems
- 289. Game of Life
- 2123. Minimum Operations to Remove Adjacent Ones in Matrix

---

## 🚀 Final Thoughts
This problem teaches the valuable technique of using the input data structure itself as auxiliary storage. The careful ordering of operations (mark -> fill -> handle boundaries) is crucial.

---

✨ **Rule to remember:**
> "When you need O(1) space for matrix problems, repurpose the first row and column as markers."
