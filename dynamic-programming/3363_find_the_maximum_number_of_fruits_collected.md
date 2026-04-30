# 3363. Find the Maximum Number of Fruits Collected

## 🔗 Problem Link
https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Matrix, Dynamic Programming

---

## 🧩 Problem Summary
Three children start at corners of an `n x n` grid: top-left `(0,0)`, top-right `(0,n-1)`, and bottom-left `(n-1,0)`. They all walk to `(n-1,n-1)`. The top-left child walks diagonally. The other two have constrained movement. Find the maximum total fruits collected without double-counting.

### 📌 Constraints
- `2 <= n <= 1000`
- `0 <= fruits[i][j] <= 1000`

---

## 💭 Intuition
👉 Decompose the problem into three independent paths: (1) top-left to bottom-right along the diagonal (fixed path), (2) top-right to bottom-right with DP, and (3) bottom-left to bottom-right with DP. Subtract double-counted `fruits[n-1][n-1]`.

---

## ⚡ Approach — Three Independent Path DPs

### 🧠 Idea
- **Top-left**: always walks along the diagonal, collecting `fruits[i][i]` for each `i`.
- **Top-right**: uses DP from `(0, n-1)` to `(n-1, n-1)`, moving diagonally down-left, straight down, or diagonally down-right, constrained to stay above the diagonal.
- **Bottom-left**: uses DP from `(n-1, 0)` to `(n-1, n-1)`, moving right-up, straight right, or right-down, constrained to stay below the diagonal.
- Total = sum of three paths - 2 * `fruits[n-1][n-1]` (counted by all three).

---

## 💻 Code

```cpp
class Solution {
 public:
  int maxCollectedFruits(vector<vector<int>>& fruits) {
    return getTopLeft(fruits) + getTopRight(fruits) + getBottomLeft(fruits) -
           2 * fruits.back().back();
  }

 private:
  int getTopLeft(const vector<vector<int>>& fruits) {
    const int n = fruits.size();
    int res = 0;
    for (int i = 0; i < n; ++i)
      res += fruits[i][i];
    return res;
  }

  int getTopRight(const vector<vector<int>>& fruits) {
    const int n = fruits.size();
    // dp[i][j] := the number of fruits collected from (0, n - 1) to (i, j)
    vector<vector<int>> dp(n, vector<int>(n));
    dp[0][n - 1] = fruits[0][n - 1];
    for (int x = 0; x < n; ++x) {
      for (int y = 0; y < n; ++y) {
        if (x >= y && !(x == n - 1 && y == n - 1))
          continue;
        for (const auto& [dx, dy] :
             vector<pair<int, int>>{{1, -1}, {1, 0}, {1, 1}}) {
          const int i = x - dx;
          const int j = y - dy;
          if (i < 0 || i == n || j < 0 || j == n)
            continue;
          if (i < j && j < n - 1 - i)
            continue;
          dp[x][y] = max(dp[x][y], dp[i][j] + fruits[x][y]);
        }
      }
    }

    return dp[n - 1][n - 1];
  }

  int getBottomLeft(const vector<vector<int>>& fruits) {
    const int n = fruits.size();
    // dp[i][j] := the number of fruits collected from (n - 1, 0) to (i, j)
    vector<vector<int>> dp(n, vector<int>(n));
    dp[n - 1][0] = fruits[n - 1][0];
    for (int y = 0; y < n; ++y) {
      for (int x = 0; x < n; ++x) {
        if (x <= y && !(x == n - 1 && y == n - 1))
          continue;
        for (const auto& [dx, dy] :
             vector<pair<int, int>>{{-1, 1}, {0, 1}, {1, 1}}) {
          const int i = x - dx;
          const int j = y - dy;
          if (i < 0 || i == n || j < 0 || j == n)
            continue;
          if (j < i && i < n - 1 - j)
            continue;
          dp[x][y] = max(dp[x][y], dp[i][j] + fruits[x][y]);
        }
      }
    }
    return dp[n - 1][n - 1];
  }
};
```

---

## 🧠 Dry Run
### Input
```
fruits = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
```
### Steps
```
TopLeft: fruits[0][0]+fruits[1][1]+fruits[2][2] = 1+5+9 = 15
TopRight: (0,2)→(1,1 or 1,2)→(2,2)
  dp[0][2]=3, dp[1][2]=max(3+6)=9, dp[2][2]=max(9+9)=18
BottomLeft: (2,0)→(2,1 or 1,1)→(2,2)
  dp[2][0]=7, dp[2][1]=max(7+8)=15, dp[2][2]=max(15+9)=24
Total = 15 + 18 + 24 - 2*9 = 39
```

---

## ⏱️ Time Complexity
```
O(n^2) — DP over the grid for each of the two non-diagonal paths
```

## 💾 Space Complexity
```
O(n^2) — DP tables
```

---

## ⚠️ Edge Cases
- `n = 2` → minimal grid, limited movement
- All fruits on the diagonal → top-right and bottom-left collect only endpoints
- Large `n` with sparse fruits → DP still runs in O(n^2)

---

## 🎯 Interview Takeaways
- Decomposing a multi-agent problem into independent subproblems simplifies DP.
- The diagonal constraint creates natural non-overlapping regions for each path.
- Be careful with double-counting at the destination.

---

## 📌 Key Pattern
👉 **"Decompose multi-path collection into independent DPs with non-overlapping regions"**

---

## 🔁 Related Problems
- 741. Cherry Pickup
- 1463. Cherry Pickup II
- 64. Minimum Path Sum

---

## 🚀 Final Thoughts
A clever decomposition into three independent paths where each child's region doesn't overlap (except at the destination). The diagonal walker has a fixed path, while the other two solve standard DP problems in their respective triangular regions.

---

✨ **Rule to remember:**
> "When multiple agents collect on a grid, decompose into independent non-overlapping regions."
