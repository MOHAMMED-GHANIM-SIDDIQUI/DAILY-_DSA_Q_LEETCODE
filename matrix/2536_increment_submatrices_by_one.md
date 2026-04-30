# 2536. Increment Submatrices by One

## 🔗 Problem Link
https://leetcode.com/problems/increment-submatrices-by-one/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Matrix, Prefix Sum

---

## 🧩 Problem Summary
You are given a positive integer `n`, representing an `n x n` matrix filled with zeroes. You are also given a list of queries where each query specifies a submatrix `[row1, col1, row2, col2]`. For each query, increment all elements inside the specified submatrix by one. Return the final matrix after processing all queries.

### 📌 Constraints
- `1 <= n <= 500`
- `1 <= queries.length <= 10^4`
- `0 <= row1 <= row2 < n`
- `0 <= col1 <= col2 < n`

---

## 💭 Intuition
👉 Instead of naively incrementing every cell in the submatrix for each query (which could be O(n^2) per query), we can use a 1D prefix sum technique on each row. For each row affected by a query, mark `+1` at the start column and `-1` after the end column, then compute the prefix sum to reconstruct the actual values.

---

## ⚡ Approach — Row-wise Prefix Sum (Difference Array)

### 🧠 Idea
- For each query `[row1, col1, row2, col2]`, iterate over rows `row1` to `row2` and apply a difference array update: `++prefix[i][col1]` and `--prefix[i][col2 + 1]`.
- After processing all queries, compute the prefix sum for each row to get the final values.

---

## 💻 Code

```cpp
class Solution {
 public:
  vector<vector<int>> rangeAddQueries(int n, vector<vector<int>>& queries) {
    vector<vector<int>> ans(n, vector<int>(n));
    vector<vector<int>> prefix(n, vector<int>(n + 1));

    for (const vector<int>& query : queries) {
      const int row1 = query[0];
      const int col1 = query[1];
      const int row2 = query[2];
      const int col2 = query[3];
      for (int i = row1; i <= row2; ++i) {
        ++prefix[i][col1];
        --prefix[i][col2 + 1];
      }
    }

    for (int i = 0; i < n; ++i) {
      int sum = 0;
      for (int j = 0; j < n; ++j) {
        sum += prefix[i][j];
        ans[i][j] = sum;
      }
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 3, queries = [[1,1,2,2],[0,0,1,1]]
```
### Steps
```
After query [1,1,2,2]:
  prefix[1] = [0, 1, 0, -1]
  prefix[2] = [0, 1, 0, -1]

After query [0,0,1,1]:
  prefix[0] = [1, 0, -1, 0]
  prefix[1] = [1, 1, -1, -1]

Prefix sum row 0: [1, 1, 0]
Prefix sum row 1: [1, 2, 1]
Prefix sum row 2: [0, 1, 1]

ans = [[1,1,0],[1,2,1],[0,1,1]]
```

---

## ⏱️ Time Complexity
```
O(n * Q + n^2) where Q is the number of queries
```

## 💾 Space Complexity
```
O(n^2)
```

---

## ⚠️ Edge Cases
- Single cell queries where `row1 == row2` and `col1 == col2`
- Overlapping queries on the same submatrix
- Queries spanning the entire matrix

---

## 🎯 Interview Takeaways
- The difference array technique converts range updates from O(n) to O(1) per update, then reconstructs with a single prefix sum pass.
- This approach applies row-by-row, so the 2D problem reduces to multiple 1D difference arrays.

---

## 📌 Key Pattern
👉 **"Difference Array / Prefix Sum for efficient range increment operations"**

---

## 🔁 Related Problems
- 370. Range Addition
- 304. Range Sum Query 2D - Immutable
- 2132. Stamping the Grid

---

## 🚀 Final Thoughts
This problem is a great exercise in applying the difference array technique in a 2D context. While a full 2D difference array is possible, the row-wise approach is simpler and sufficient here.

---

✨ **Rule to remember:**
> Use a difference array when you need to perform many range increments and only need the final result — mark boundaries, then prefix sum.
