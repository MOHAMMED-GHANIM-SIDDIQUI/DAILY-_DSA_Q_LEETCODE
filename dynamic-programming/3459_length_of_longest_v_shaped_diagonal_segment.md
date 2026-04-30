# 3459. Length of Longest V-Shaped Diagonal Segment

## 🔗 Problem Link
https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Matrix, DFS, Memoization, Dynamic Programming

---

## 🧩 Problem Summary
Given an m x n grid containing 0, 1, and 2, find the length of the longest "V-shaped" diagonal segment. A V-shaped segment starts at a cell with value 1, moves diagonally alternating between 2 and 0, and is allowed to make at most one 90-degree turn (clockwise) during its path.

### 📌 Constraints
- 2 <= m, n <= 500
- grid[i][j] is 0, 1, or 2

---

## 💭 Intuition
👉 Starting from every cell with value 1, try all 4 diagonal directions. Use DFS with memoization to extend the path (alternating 2→0→2→...) and optionally make one clockwise turn. The state is (i, j, turned, expected_num, direction).

---

## ⚡ Approach — DFS with 5D Memoization

### 🧠 Idea
- For each cell (i,j) with value 1, try all 4 diagonal directions.
- DFS extends the path: if current cell matches expected value, continue.
- At each step, optionally turn clockwise (if not already turned).
- Expected values alternate: 1 → 2 → 0 → 2 → 0 → ...
- Memoize on (i, j, turned, hashNum, direction) to avoid recomputation.
- Return 1 + max(continue straight, turn) at each cell.

---

## 💻 Code

```cpp
class Solution {
 public:
  int lenOfVDiagonal(vector<vector<int>>& grid) {
    const int m = grid.size();
    const int n = grid[0].size();
    vector<vector<vector<vector<vector<int>>>>> mem(
        m, vector<vector<vector<vector<int>>>>(
               n, vector<vector<vector<int>>>(
                      2, vector<vector<int>>(2, vector<int>(4, -1)))));
    int res = 0;

    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j)
        if (grid[i][j] == 1)
          for (int d = 0; d < 4; ++d) {
            const auto& [dx, dy] = kDirs[d];
            res = max(res, 1 + dfs(grid, i + dx, j + dy, /*turned=*/false, 2, d,
                                   mem));
          }

    return res;
  }

 private:
  static constexpr int kDirs[4][2] = {{-1, 1}, {1, 1}, {1, -1}, {-1, -1}};

  int dfs(const vector<vector<int>>& grid, int i, int j, bool turned, int num,
          int dir, vector<vector<vector<vector<vector<int>>>>>& mem) {
    if (i < 0 || i == grid.size() || j < 0 || j == grid[0].size())
      return 0;
    if (grid[i][j] != num)
      return 0;

    const int hashNum = max(0, num - 1);
    if (mem[i][j][turned][hashNum][dir] != -1)
      return mem[i][j][turned][hashNum][dir];

    const int nextNum = num == 2 ? 0 : 2;
    const auto& [dx, dy] = kDirs[dir];
    int res = 1 + dfs(grid, i + dx, j + dy, turned, nextNum, dir, mem);

    if (!turned) {
      const int nextDir = (dir + 1) % 4;
      const auto& [nextDx, nextDy] = kDirs[nextDir];
      res = max(res, 1 + dfs(grid, i + nextDx, j + nextDy, /*turned=*/true,
                             nextNum, nextDir, mem));
    }

    return mem[i][j][turned][hashNum][dir] = res;
  }
};
```

---

## 🧠 Dry Run
### Input
```
grid = [[1, 2, 0],
        [0, 0, 2],
        [2, 0, 1]]
```
### Steps
```
Starting at (0,0) with value 1, direction (1,1) [SE]:
  (1,1)=0? need 2 → stop. Length = 1

Starting at (2,2) with value 1, direction (-1,-1) [NW]:
  (1,1)=0? need 2 → stop. Length = 1

Starting at (2,2) with value 1, direction (-1,1) [NE]:
  (1,3) out of bounds → stop. Length = 1

Starting at (0,0) with value 1, direction (1,-1) [SW]:
  (1,-1) out of bounds → stop. Length = 1

Result: 1 (simple case, no long V-paths)
```

---

## ⏱️ Time Complexity
```
O(m * n * 2 * 2 * 4) = O(m * n) — each state computed at most once
```

## 💾 Space Complexity
```
O(m * n * 16) = O(m * n) — 5D memoization table
```

---

## ⚠️ Edge Cases
- No cell with value 1 → return 0
- V-path of length 1 (just the starting cell)
- Turn at the very first step vs. turn later
- Grid boundaries cutting paths short

---

## 🎯 Interview Takeaways
- Multi-dimensional memoization is necessary when state depends on position, direction, turn status, and expected value.
- The "at most one turn" constraint adds a boolean dimension to the DP state.
- Diagonal directions can be encoded as an array of (dx, dy) pairs with clockwise ordering.

---

## 📌 Key Pattern
👉 **"DFS with multi-dimensional memoization for constrained path problems"**

---

## 🔁 Related Problems
- 329. Longest Increasing Path in a Matrix
- 1219. Path with Maximum Gold
- 489. Robot Room Cleaner

---

## 🚀 Final Thoughts
This is a challenging matrix DFS problem with a complex state space. The 5D memoization might seem daunting, but each dimension corresponds to a natural part of the state: position, turn status, expected value, and direction.

---

✨ **Rule to remember:**
> When a path problem has constraints on direction, turns, and value patterns, encode each constraint as a memoization dimension.
