# 1559. Detect Cycles in 2D Grid

## 🔗 Problem Link
https://leetcode.com/problems/detect-cycles-in-2d-grid/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Depth-First Search, Breadth-First Search, Union Find, Matrix

---

## 🧩 Problem Summary
Given a 2D grid of characters, determine if there exists a cycle in the grid. A cycle is a path of length 4 or more that starts and ends at the same cell, where consecutive cells are horizontally or vertically adjacent and have the same character.

### 📌 Constraints
- `1 <= m, n <= 500` (grid dimensions)
- `grid[i][j]` is a lowercase English letter.

---

## 💭 Intuition
👉 Use DFS to traverse cells with the same character. If we revisit a cell that is already in the current DFS traversal (and it's not the parent we just came from), we've found a cycle. Track visited cells globally to avoid redundant searches.

---

## ⚡ Approach — DFS with Parent Tracking

### 🧠 Idea
- For each unvisited cell, start a DFS exploring only cells with the same character.
- Track the parent cell `(pi, pj)` to avoid immediately going back.
- If we reach a cell that's already been visited (in `seen` set) and it's not the parent, a cycle exists.
- Use a global `seen` set so each cell is processed only once.

---

## 💻 Code

```python
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        seen = set()
        def dfs(i, j, pi, pj, char):
            if (i, j) in seen:
                return True
            seen.add((i, j))
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= ni < n and 0 <= nj < m:
                    if (ni, nj) == (pi, pj):
                        continue
                    if grid[ni][nj] == char:
                        if dfs(ni, nj, i, j, char):
                            return True
            return False
        for i in range(n):
            for j in range(m):
                if (i, j) not in seen:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True
        return False
```

---

## 🧠 Dry Run
### Input
```
grid = [["a","a","a","a"],
        ["a","b","b","a"],
        ["a","b","b","a"],
        ["a","a","a","a"]]
```
### Steps
```
Start DFS at (0,0), char='a'
Visit: (0,0)→(0,1)→(0,2)→(0,3)→(1,3)→(2,3)→(3,3)→(3,2)→(3,1)→(3,0)→(2,0)→(1,0)
From (1,0), neighbor (0,0) is in seen and not parent (2,0) → cycle found!
Answer: True
```

---

## ⏱️ Time Complexity
```
O(m * n), each cell is visited at most once
```

## 💾 Space Complexity
```
O(m * n) for the seen set and recursion stack
```

---

## ⚠️ Edge Cases
- No same-character neighbors — no cycles possible.
- 1x1 grid — no cycle possible (need length >= 4).
- Entire grid same character — almost certainly has a cycle if grid is at least 2x2.
- Very large grid — recursion depth may be an issue (Python's default limit); iterative DFS or Union-Find may be needed.

---

## 🎯 Interview Takeaways
- Cycle detection in undirected graphs uses parent tracking to avoid false positives from the edge we just traversed.
- The `seen` set serves dual purpose: marks visited for cycle detection AND prevents redundant DFS starts.
- Union-Find is an alternative approach that avoids recursion depth issues.

---

## 📌 Key Pattern
👉 **"DFS cycle detection in undirected graph — revisiting a non-parent node means a cycle exists"**

---

## 🔁 Related Problems
- 200 — Number of Islands
- 684 — Redundant Connection
- 785 — Is Graph Bipartite?

---

## 🚀 Final Thoughts
This problem applies standard undirected graph cycle detection to a 2D grid. The critical detail is skipping the parent cell during DFS to avoid detecting the trivial 2-node "cycle." Each connected component of same-character cells is checked independently.

---

✨ **Rule to remember:**
> "In undirected graph DFS, a cycle exists if you reach an already-visited node that is not your parent."
