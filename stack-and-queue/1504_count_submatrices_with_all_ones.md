# 1504. Count Submatrices With All Ones

## 🔗 Problem Link
https://leetcode.com/problems/count-submatrices-with-all-ones/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Dynamic Programming, Stack, Matrix

---

## 🧩 Problem Summary
Given an `m x n` binary matrix `mat`, return the number of submatrices that have all ones. A submatrix is any contiguous rectangular region of the matrix.

### 📌 Constraints
- `1 <= m, n <= 150`
- `mat[i][j]` is either `0` or `1`.

---

## 💭 Intuition
👉 For each pair of rows (top row to bottom row), compress the columns into a 1D array where each entry is 1 only if all elements in that column between the two rows are 1. Then count the number of contiguous all-ones subarrays in that 1D array — each such subarray corresponds to a valid submatrix.

---

## ⚡ Approach — Row Compression + Linear Count

### 🧠 Idea
- Fix a top row (`baseRow`) and expand downward row by row.
- Maintain a compressed row using bitwise AND to track which columns remain all-ones.
- For each expanded row, count contiguous segments of 1's in the compressed row.
- The count of subarrays in a segment of length `L` is `L*(L+1)/2`, computed incrementally.

---

## 💻 Code

```cpp
class Solution {
 public:
  int numSubmat(vector<vector<int>>& mat) {
    const int m = mat.size();
    const int n = mat[0].size();
    int ans = 0;

    for (int baseRow = 0; baseRow < m; ++baseRow) {
      vector<int> row(n, 1);
      for (int i = baseRow; i < m; ++i) {
        for (int j = 0; j < n; ++j)
          row[j] &= mat[i][j];
        ans += count(row);
      }
    }

    return ans;
  }

 private:
  int count(vector<int>& row) {
    int res = 0;
    int length = 0;
    for (const int num : row) {
      length = num == 0 ? 0 : length + 1;
      res += length;
    }
    return res;
  }
};
```

---

## 🧠 Dry Run
### Input
```
mat = [[1,0,1],
       [1,1,0],
       [1,1,0]]
```
### Steps
```
baseRow=0:
  i=0: row=[1,0,1], count → lengths: 1,0,1 → res=1+0+1=2, ans=2
  i=1: row=[1,0,0], count → lengths: 1,0,0 → res=1, ans=3
  i=2: row=[1,0,0], count → lengths: 1,0,0 → res=1, ans=4
baseRow=1:
  i=1: row=[1,1,0], count → lengths: 1,2,0 → res=3, ans=7
  i=2: row=[1,1,0], count → lengths: 1,2,0 → res=3, ans=10
baseRow=2:
  i=2: row=[1,1,0], count → lengths: 1,2,0 → res=3, ans=13
Answer: 13
```

---

## ⏱️ Time Complexity
```
O(m^2 * n), iterating over all row pairs and columns
```

## 💾 Space Complexity
```
O(n) for the compressed row
```

---

## ⚠️ Edge Cases
- All zeros — answer is 0.
- All ones — answer is `m*(m+1)/2 * n*(n+1)/2`.
- Single row or single column — reduces to counting contiguous 1's.

---

## 🎯 Interview Takeaways
- Compressing a 2D problem into 1D by fixing row ranges is a powerful technique.
- The `count` helper efficiently counts subarrays by tracking consecutive length.
- Bitwise AND naturally handles column compression for all-ones detection.

---

## 📌 Key Pattern
👉 **"Fix top row, expand downward with AND compression, count contiguous 1-subarrays"**

---

## 🔁 Related Problems
- 85 — Maximal Rectangle
- 221 — Maximal Square
- 1277 — Count Square Submatrices with All Ones

---

## 🚀 Final Thoughts
This problem demonstrates how 2D matrix problems can often be reduced to 1D subproblems by fixing one dimension. The row compression with AND and linear subarray counting keeps the solution clean and efficient.

---

✨ **Rule to remember:**
> "To count all-ones submatrices, compress rows with AND and count contiguous 1-segments for each row range."
