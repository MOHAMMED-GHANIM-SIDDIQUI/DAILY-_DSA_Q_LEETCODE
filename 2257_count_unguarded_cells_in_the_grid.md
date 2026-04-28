# 2257. Count Unguarded Cells in the Grid

## 🔗 Problem Link
https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Matrix, Simulation

---

## 🧩 Problem Summary
Given an `m x n` grid with guards and walls at specified positions, guards can see in four cardinal directions until blocked by a wall or another guard. Count the number of cells that are not guarded, not a wall, and not a guard.

### 📌 Constraints
- `1 <= m, n <= 10^5`
- `2 <= m * n <= 10^5`
- `1 <= guards.length, walls.length <= 5 * 10^4`

---

## 💭 Intuition
👉 Simulate each guard's line of sight in all four directions, marking cells as guarded until hitting a wall or another guard. Then count unmarked cells.

---

## ⚡ Approach — Grid Simulation

### 🧠 Idea
- Initialize a grid with 0 (empty), -1 (wall), 1 (guard).
- For each guard, extend in all 4 directions and mark cells as 2 (guarded), stopping at walls or guards.
- Count cells still marked 0.

---

## 💻 Code

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        // 0 = empty, -1 = wall, 1 = guard, 2 = guarded
        vector<vector<int>> grid(m, vector<int>(n, 0));

        // Mark walls
        for (auto &p : walls) {
            grid[p[0]][p[1]] = -1;
        }

        // Mark guards
        for (auto &p : guards) {
            grid[p[0]][p[1]] = 1;
        }

        // Directions: up, down, left, right
        vector<vector<int>> dirs = {{-1,0},{1,0},{0,-1},{0,1}};

        // Mark all guarded cells
        for (auto &g : guards) {
            for (auto &d : dirs) {
                int x = g[0] + d[0];
                int y = g[1] + d[1];
                while (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] != -1 && grid[x][y] != 1) {
                    if (grid[x][y] == 0) grid[x][y] = 2;
                    x += d[0];
                    y += d[1];
                }
            }
        }

        // Count unguarded cells
        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) ans++;
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
m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
```
### Steps
```
Grid after marking guards (1) and walls (-1):
[1, -1, 0, 0, 0, 0]
[0,  1, 0, 0,-1, 0]
[0,  0,-1, 1, 0, 0]
[0,  0, 0, 0, 0, 0]

After guard (0,0) extends down and right (right blocked by wall):
Guard (1,1) extends up, down, left, right (right blocked by wall at (1,4))
Guard (2,3) extends all 4 dirs (left blocked by wall at (2,2))

Count cells still 0 → answer
```

---

## ⏱️ Time Complexity
```
O(m * n) — grid initialization and final count; guard simulation is bounded by grid size
```

## 💾 Space Complexity
```
O(m * n) — for the grid
```

---

## ⚠️ Edge Cases
- No guards → all non-wall cells are unguarded
- No walls → guards see entire rows/columns
- Guard next to another guard → sight stops immediately

---

## 🎯 Interview Takeaways
- Grid simulation with directional ray-casting is a common pattern.
- Using different integer markers (0, -1, 1, 2) avoids extra data structures.
- Walls and guards both block line of sight — handle both as stop conditions.

---

## 📌 Key Pattern
👉 **"Ray-cast from each source in four directions, marking cells until blocked"**

---

## 🔁 Related Problems
- 361. Bomb Enemy
- 1252. Cells with Odd Values in a Matrix
- 999. Available Captures for Rook

---

## 🚀 Final Thoughts
A clean simulation problem where the key is correctly handling the blocking conditions. The ray-casting approach from each guard is intuitive and efficient within the given constraints.

---

✨ **Rule to remember:**
> "Ray-cast from guards in 4 directions, stop at walls and other guards, then count unmarked cells."
