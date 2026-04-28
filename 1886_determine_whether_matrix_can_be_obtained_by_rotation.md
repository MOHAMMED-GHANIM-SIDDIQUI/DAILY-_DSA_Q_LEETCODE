# 1886. Determine Whether Matrix Can Be Obtained By Rotation

## 🔗 Problem Link
https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Array, Matrix

---

## 🧩 Problem Summary
Given two `n x n` binary matrices `mat` and `target`, return `true` if it is possible to make `mat` equal to `target` by rotating `mat` in 90-degree increments (0, 90, 180, or 270 degrees).

### 📌 Constraints
- `n == mat.length == target.length`
- `1 <= n <= 10`
- `mat[i][j]` and `target[i][j]` are either `0` or `1`

---

## 💭 Intuition
👉 There are only 4 possible rotations (0°, 90°, 180°, 270°). Rotate the matrix up to 4 times and check for equality each time.

---

## ⚡ Approach — Rotate and Compare

### 🧠 Idea
- Implement a 90-degree clockwise rotation: transpose the matrix, then reverse each row.
- Apply the rotation up to 4 times, checking after each rotation if the result equals `target`.
- Return `True` if any rotation matches, `False` otherwise.

---

## 💻 Code

```python
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rot90(org_mat):
            for  i in range(len(org_mat)):
                for j in range(i,len(org_mat[0])):
                    org_mat[i][j] , org_mat[j][i] = org_mat[j][i] , org_mat[i][j]
            row_num = 0
            for row in org_mat:
                org_mat[row_num] = row[::-1]
                row_num+=1
            return org_mat


        for i in range(4):
            if rot90(mat) == target:
                return True
        return False
```

---

## 🧠 Dry Run
### Input
```
mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
```
### Steps
```
Rotation 1 (90°):
  Transpose: [[0,1],[1,0]] → [[0,1],[1,0]]
  Reverse rows: [[1,0],[0,1]]
  Compare with target [[1,0],[0,1]] → Match! Return True
```

---

## ⏱️ Time Complexity
```
O(n^2) per rotation, up to 4 rotations → O(n^2)
```

## 💾 Space Complexity
```
O(n) for row reversal (in-place transpose)
```

---

## ⚠️ Edge Cases
- `mat` already equals `target` (0° rotation) — note this code rotates first, so 4 rotations cover all cases including returning to original
- 1x1 matrix → always `True`
- No rotation matches → return `False`

---

## 🎯 Interview Takeaways
- 90° clockwise rotation = transpose + reverse each row.
- With only 4 possible rotations, brute force is efficient and clean.
- In-place matrix manipulation requires careful index management.

---

## 📌 Key Pattern
👉 **"Rotate matrix 90° clockwise by transposing then reversing rows"**

---

## 🔁 Related Problems
- 48. Rotate Image
- 867. Transpose Matrix
- 2022. Convert 1D Array Into 2D Array

---

## 🚀 Final Thoughts
This problem directly tests knowledge of matrix rotation mechanics. The transpose-then-reverse technique is a must-know for matrix manipulation problems.

---

✨ **Rule to remember:**
> 90° clockwise rotation = transpose + reverse each row. Check all 4 rotations.
