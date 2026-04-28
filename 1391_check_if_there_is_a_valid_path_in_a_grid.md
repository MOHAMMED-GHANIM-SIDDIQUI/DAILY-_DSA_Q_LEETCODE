# 1391. Check if There is a Valid Path in a Grid

## 🔗 Problem Link
https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Depth-First Search, Breadth-First Search, Matrix

---

## 🧩 Problem Summary
Given an `m x n` grid where each cell contains a street (numbered 1-6) with specific connection directions, determine if there is a valid path from the upper-left cell `(0,0)` to the lower-right cell `(m-1, n-1)`. A path is valid only if consecutive cells are connected through matching openings.

### 📌 Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `1 <= grid[i][j] <= 6`

---

## 💭 Intuition
👉 Each street type defines which directions it connects to. A move from cell A to cell B is valid only if A has an opening toward B AND B has an opening back toward A. DFS with this bidirectional check solves the problem.

---

## ⚡ Approach — DFS with Bidirectional Connection Check

### 🧠 Idea
- Map each street type to its two connection directions.
- From each cell, try moving in both allowed directions.
- For each neighbor, verify it has a direction pointing back to the current cell.
- Use a visited set to avoid cycles; DFS until reaching `(m-1, n-1)`.

---

## 💻 Code

```python
class Solution:
    def hasValidPath(self, grid):
        self.m = len(grid)
        self.n = len(grid[0])

        self.directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(-1, 0), (0, 1)]
        }

        visited = set()
        return self.dfs(grid, 0, 0, visited)

    def dfs(self, grid, i, j, visited):
        if i == self.m - 1 and j == self.n - 1:
            return True

        visited.add((i, j))

        for di, dj in self.directions[grid[i][j]]:
            ni, nj = i + di, j + dj

            if not (0 <= ni < self.m and 0 <= nj < self.n):
                continue
            if (ni, nj) in visited:
                continue

            # check back connection
            for bi, bj in self.directions[grid[ni][nj]]:
                if ni + bi == i and nj + bj == j:
                    if self.dfs(grid, ni, nj, visited):
                        return True

        return False
```

---

## 🧠 Dry Run
### Input
```
grid = [[2,4,3],[6,5,2]]
```
### Steps
```
Start at (0,0), street=2 → directions: up(-1,0), down(1,0)
  Try up → out of bounds
  Try down → (1,0), street=6 → directions: up(-1,0), right(0,1)
    Back check: (1,0)+(-1,0)=(0,0) ✓ → DFS(1,0)
    At (1,0), street=6 → right(0,1) → (1,1), street=5
      Back check: (1,1)+(0,-1)=(1,0) ✓ → DFS(1,1)
      At (1,1), street=5 → up(-1,0) → (0,1), street=4
        Back check: (0,1)+(1,0)=(1,1) ✓ → DFS(0,1)
        ... continues to (m-1,n-1) → True
```

---

## ⏱️ Time Complexity
```
O(m * n) — each cell is visited at most once
```

## 💾 Space Complexity
```
O(m * n) — for the visited set and recursion stack
```

---

## ⚠️ Edge Cases
- `1x1` grid → already at destination, return `True`
- Grid where start cell points away from the only possible path
- Large grids requiring deep recursion (may need iterative DFS or BFS)

---

## 🎯 Interview Takeaways
- Bidirectional connection validation is the key insight — both cells must agree on the connection.
- Mapping street types to direction vectors simplifies the logic significantly.
- DFS/BFS are interchangeable here; both work in O(m*n).

---

## 📌 Key Pattern
👉 **"Graph traversal with bidirectional edge validation — both endpoints must confirm the connection."**

---

## 🔁 Related Problems
- 490. The Maze
- 1203. Sort Items by Groups Respecting Dependencies
- 200. Number of Islands

---

## 🚀 Final Thoughts
The problem looks complex with six street types, but reducing each to a pair of direction vectors and enforcing bidirectional connectivity makes it a standard graph traversal.

---

✨ **Rule to remember:**
> In grid path problems with directional constraints, always verify connections from both sides.
