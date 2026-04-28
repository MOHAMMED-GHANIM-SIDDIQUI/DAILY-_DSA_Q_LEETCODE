# 3446. Sort Matrix by Diagonals

## 🔗 Problem Link
https://leetcode.com/problems/sort-matrix-by-diagonals/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Matrix, Sorting

---

## 🧩 Problem Summary
Given an n x n matrix, sort each diagonal independently. Diagonals in the bottom-left triangle (including the main diagonal) are sorted in ascending order, and diagonals in the top-right triangle are sorted in descending order.

### 📌 Constraints
- 1 <= n <= 100
- 1 <= grid[i][j] <= 10^5

---

## 💭 Intuition
👉 Group matrix elements by their diagonal index (i - j). All cells on the same diagonal share the same i - j value. Sort each diagonal group according to the rule (ascending for bottom-left, descending for top-right), then fill back.

---

## ⚡ Approach — Diagonal Grouping + Sorting

### 🧠 Idea
- Use diagonal index d = i - j + n to avoid negative indices.
- Collect all elements on each diagonal.
- If d < n (top-right triangle), sort descending; otherwise sort ascending.
- Fill the matrix back by popping from the sorted lists.

---

## 💻 Code

```cpp
class Solution {
 public:
  vector<vector<int>> sortMatrix(vector<vector<int>>& grid) {
    const int n = grid.size();
    vector<vector<int>> ans(n, vector<int>(n));
    vector<vector<int>> diag(2 * n + 1);

    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j)
        diag[i - j + n].push_back(grid[i][j]);

    for (int i = 0; i < 2 * n + 1; ++i)
      if (i < n)
        ranges::sort(diag[i], greater<int>());
      else
        ranges::sort(diag[i]);

    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j)
        ans[i][j] = diag[i - j + n].back(), diag[i - j + n].pop_back();

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
grid = [[1,7,3],
        [9,8,2],
        [4,5,6]]
```
### Steps
```
n=3, diagonals indexed by i-j+3:
d=1 (i-j=-2): [3]         → top-right, sort desc: [3]
d=2 (i-j=-1): [7,2]       → top-right, sort desc: [7,2]
d=3 (i-j=0):  [1,8,6]     → main+below, sort asc: [1,6,8]
d=4 (i-j=1):  [9,5]       → below, sort asc: [5,9]
d=5 (i-j=2):  [4]         → below, sort asc: [4]

Fill back (pop from back):
ans[0][0]=diag[3].pop=8, ans[0][1]=diag[2].pop=2, ans[0][2]=diag[1].pop=3
ans[1][0]=diag[4].pop=9, ans[1][1]=diag[3].pop=6, ans[1][2]=diag[2].pop=7
ans[2][0]=diag[5].pop=4, ans[2][1]=diag[4].pop=5, ans[2][2]=diag[3].pop=1

Result: [[8,2,3],[9,6,7],[4,5,1]]
```

---

## ⏱️ Time Complexity
```
O(n^2 log n) — sorting diagonals of length up to n
```

## 💾 Space Complexity
```
O(n^2) — for diagonal storage and result matrix
```

---

## ⚠️ Edge Cases
- 1x1 matrix → return as-is
- All elements the same → sorting has no effect
- Main diagonal (i == j) is sorted ascending

---

## 🎯 Interview Takeaways
- Diagonal index i - j uniquely identifies each diagonal.
- Grouping by diagonal index and sorting independently is a clean pattern.
- Pop-back during fill ensures elements are placed in the right order.

---

## 📌 Key Pattern
👉 **"Group by diagonal index (i - j), sort independently"**

---

## 🔁 Related Problems
- 498. Diagonal Traverse
- 1329. Sort the Matrix Diagonally

---

## 🚀 Final Thoughts
A straightforward matrix problem once you recognize the i - j diagonal grouping. The only twist is the different sort orders for upper vs lower triangles.

---

✨ **Rule to remember:**
> Elements on the same diagonal share the same (i - j) value — group, sort, and refill.
