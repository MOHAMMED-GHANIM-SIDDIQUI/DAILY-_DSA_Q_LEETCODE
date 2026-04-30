# 2435. Paths in Matrix Whose Sum Is Divisible by K

## 🔗 Problem Link
https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Dynamic Programming, Matrix

---

## 🧩 Problem Summary
Given an `m x n` grid of integers and an integer `k`, count the number of paths from top-left to bottom-right (moving only right or down) where the sum of elements along the path is divisible by `k`. Return the result modulo 10^9 + 7.

### 📌 Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 5 * 10^4`
- `1 <= m * n <= 5 * 10^4`
- `0 <= grid[i][j] <= 10^9`
- `1 <= k <= 50`

---

## 💭 Intuition
👉 Track the remainder of the path sum modulo `k` at each cell. Use 3D DP where `dp[i][j][r]` = number of paths to cell `(i,j)` with path sum % k == r.

---

## ⚡ Approach — 3D DP with Modular Tracking

### 🧠 Idea
- `dp[i][j][sum]` = number of paths to `(i,j)` where path sum mod `k` equals `sum`.
- Base case: `dp[0][0][grid[0][0] % k] = 1`.
- Transition: for each cell, add contributions from the cell above and the cell to the left, updating the remainder after adding `grid[i][j]`.
- Answer: `dp[m-1][n-1][0]`.

---

## 💻 Code

```cpp
class Solution {
 public:
  int numberOfPaths(vector<vector<int>>& grid, int k) {
    constexpr int kMod = 1'000'000'007;
    const int m = grid.size();
    const int n = grid[0].size();
    // dp[i][j][sum] : = the number of paths to(i, j), where the sum / k == sum
    vector<vector<vector<int>>> dp(m, vector<vector<int>>(n, vector<int>(k)));
    dp[0][0][grid[0][0] % k] = 1;

    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j)
        for (int sum = 0; sum < k; ++sum) {
          const int newSum = (sum + grid[i][j]) % k;
          if (i > 0)
            dp[i][j][newSum] += dp[i - 1][j][sum];
          if (j > 0)
            dp[i][j][newSum] += dp[i][j - 1][sum];
          dp[i][j][newSum] %= kMod;
        }

    return dp[m - 1][n - 1][0];
  }
};
```

---

## 🧠 Dry Run
### Input
```
grid = [[5,2,4],[3,0,5],[0,7,2]], k = 3
```
### Steps
```
dp[0][0][5%3=2] = 1
dp[0][1]: from left dp[0][0]. sum=2, newSum=(2+2)%3=1. dp[0][1][1]=1
dp[0][2]: from left dp[0][1]. sum=1, newSum=(1+4)%3=2. dp[0][2][2]=1
dp[1][0]: from above dp[0][0]. sum=2, newSum=(2+3)%3=2. dp[1][0][2]=1
...continue filling...
dp[2][2][0] = number of paths with sum divisible by 3.

Result: 2
```

---

## ⏱️ Time Complexity
```
O(m * n * k) — iterate over all cells and all possible remainders.
```

## 💾 Space Complexity
```
O(m * n * k) — 3D DP array.
```

---

## ⚠️ Edge Cases
- `k = 1`: all paths are valid (every sum is divisible by 1).
- Single cell grid: check if `grid[0][0] % k == 0`.
- Very large grid values: modular arithmetic handles this.

---

## 🎯 Interview Takeaways
- Adding a "remainder" dimension to path DP handles divisibility constraints.
- The state space is manageable because `k <= 50`.
- This pattern generalizes to any "count paths with sum satisfying condition" problem.

---

## 📌 Key Pattern
👉 **"Add a modular remainder dimension to grid DP to track divisibility."**

---

## 🔁 Related Problems
- 62. Unique Paths
- 64. Minimum Path Sum
- 1444. Number of Ways of Cutting a Pizza

---

## 🚀 Final Thoughts
This is a natural extension of the classic grid path DP. By adding the remainder as a third dimension, we efficiently track which path sums are divisible by k without enumerating all sums.

---

✨ **Rule to remember:**
> "Track remainder mod k as a DP dimension — it keeps the state space bounded."
