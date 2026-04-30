# 1039. Minimum Score Triangulation of Polygon

## 🔗 Problem Link
https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Dynamic Programming

---

## 🧩 Problem Summary

Given a convex polygon with `n` vertices where each vertex has a value, triangulate the polygon into `n-2` triangles. The score of a triangle is the product of its three vertex values. Return the minimum total score of all triangles in a triangulation.

### 📌 Constraints
- `n == values.length`
- `3 <= n <= 50`
- `1 <= values[i] <= 100`

---

## 💭 Intuition

👉 For any edge `(i, j)` of the polygon, we must pick a third vertex `k` between `i` and `j` to form a triangle. This splits the polygon into the triangle `(i, k, j)` and two smaller sub-polygons `(i..k)` and `(k..j)`.

👉 This is a classic interval DP problem — similar to matrix chain multiplication.

---

## ⚡ Approach — Interval DP

### 🧠 Idea
- `dp[i][j]` = minimum score to triangulate the sub-polygon from vertex `i` to vertex `j`.
- For each pair `(i, j)` with `j - i >= 2`, try every possible vertex `k` between them.
- Recurrence: `dp[i][j] = min(dp[i][k] + values[i]*values[k]*values[j] + dp[k][j])` for all `k` in `(i+1, j-1)`.
- Answer is `dp[0][n-1]`.

---

## 💻 Code

```cpp
class Solution {
 public:
  int minScoreTriangulation(vector<int>& values) {
    const int n = values.size();
    vector<vector<int>> dp(n, vector<int>(n));

    for (int j = 2; j < n; ++j)
      for (int i = j - 2; i >= 0; --i) {
        dp[i][j] = INT_MAX;
        for (int k = i + 1; k < j; ++k)
          dp[i][j] =
              min(dp[i][j],
                  dp[i][k] + values[i] * values[k] * values[j] + dp[k][j]);
      }

    return dp[0][n - 1];
  }
};
```

---

## 🧠 Dry Run

### Input
```
values = [1, 2, 3]
```

### Steps
```
n = 3, only one triangle possible: (0, 1, 2)
j=2, i=0:
  k=1: dp[0][2] = dp[0][1] + 1*2*3 + dp[1][2]
                 = 0 + 6 + 0 = 6
Output: 6
```

---

## ⏱️ Time Complexity
```
O(n^3)
```
Three nested loops: two for the interval endpoints, one for the split point.

---

## 💾 Space Complexity
```
O(n^2)
```
The 2D DP table stores results for all sub-polygons.

---

## ⚠️ Edge Cases
- `n = 3` → only one triangle, return the product of all three values.
- All values equal → any triangulation yields the same score.
- Large vertex values → products can be large but fit in int (max 100^3 * 48 triangles).

---

## 🎯 Interview Takeaways
- This is a classic interval DP pattern, analogous to matrix chain multiplication.
- The key insight is fixing an edge and choosing the third vertex.
- Iteration order matters: process shorter intervals before longer ones.
- Understanding the sub-problem decomposition is crucial.

---

## 📌 Key Pattern
👉 **"Interval DP — fix one edge, enumerate the third vertex to split into smaller sub-problems."**

---

## 🔁 Related Problems
- 312 - Burst Balloons
- 1000 - Minimum Cost to Merge Stones
- 546 - Remove Boxes

---

## 🚀 Final Thoughts
A beautiful interval DP problem that directly mirrors matrix chain multiplication. Once you see the sub-problem structure of splitting a polygon along a triangle, the recurrence follows naturally.

---

✨ **Rule to remember:**
> "Polygon triangulation = interval DP: fix an edge, pick a third vertex, and recurse on the two resulting sub-polygons."
