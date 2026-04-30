# 417. Pacific Atlantic Water Flow

## 🔗 Problem Link
https://leetcode.com/problems/pacific-atlantic-water-flow/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Depth-First Search, Breadth-First Search, Matrix

---

## 🧩 Problem Summary
Given an m x n matrix of heights representing an island, water can flow from a cell to adjacent cells with equal or lower height. The Pacific ocean touches the left and top edges, and the Atlantic ocean touches the right and bottom edges. Find all cells from which water can flow to both oceans.

### 📌 Constraints
- `m == heights.length`
- `n == heights[r].length`
- `1 <= m, n <= 200`
- `0 <= heights[r][c] <= 10^5`

---

## 💭 Intuition
👉 Instead of flowing from each cell to the ocean, reverse the direction: start DFS from each ocean's border and flow uphill. Cells reachable from both oceans are the answer.

---

## ⚡ Approach — Reverse DFS from Both Oceans

### 🧠 Idea
- Create two visited matrices: `seenP` (Pacific) and `seenA` (Atlantic).
- Run DFS from all Pacific border cells (top row and left column), marking reachable cells.
- Run DFS from all Atlantic border cells (bottom row and right column), marking reachable cells.
- Cells marked in both matrices can reach both oceans.

---

## 💻 Code

```cpp
class Solution {
 public:
  vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
    const int m = heights.size();
    const int n = heights[0].size();
    vector<vector<int>> ans;
    vector<vector<bool>> seenP(m, vector<bool>(n));
    vector<vector<bool>> seenA(m, vector<bool>(n));

    for (int i = 0; i < m; ++i) {
      dfs(heights, i, 0, seenP);
      dfs(heights, i, n - 1, seenA);
    }

    for (int j = 0; j < n; ++j) {
      dfs(heights, 0, j, seenP);
      dfs(heights, m - 1, j, seenA);
    }

    for (int i = 0; i < m; ++i)
      for (int j = 0; j < n; ++j)
        if (seenP[i][j] && seenA[i][j])
          ans.push_back({i, j});

    return ans;
  }

 private:
  void dfs(const vector<vector<int>>& heights, int i, int j,
           vector<vector<bool>>& seen, int h = 0) {
    if (i < 0 || i == heights.size() || j < 0 || j == heights[0].size())
      return;
    if (seen[i][j] || heights[i][j] < h)
      return;

    seen[i][j] = true;
    dfs(heights, i + 1, j, seen, heights[i][j]);
    dfs(heights, i - 1, j, seen, heights[i][j]);
    dfs(heights, i, j + 1, seen, heights[i][j]);
    dfs(heights, i, j - 1, seen, heights[i][j]);
  }
};
```

---

## 🧠 Dry Run
### Input
```
heights = [[1,2,2,3,5],
           [3,2,3,4,4],
           [2,4,5,3,1],
           [6,7,1,4,5],
           [5,1,1,2,4]]
```
### Steps
```
Pacific DFS from left column and top row:
  Starting (0,0)=1: reaches cells that flow to Pacific
  Starting (0,1)=2: etc.
Atlantic DFS from right column and bottom row:
  Starting (4,4)=4: reaches cells that flow to Atlantic
Intersection: cells reachable from both
Result: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

---

## ⏱️ Time Complexity
```
O(m * n) — each cell is visited at most twice (once per ocean)
```

## 💾 Space Complexity
```
O(m * n) — for the two visited matrices and recursion stack
```

---

## ⚠️ Edge Cases
- Single cell — always reaches both oceans.
- All cells same height — every cell reaches both oceans.
- Strictly decreasing from top-left to bottom-right — only corners may reach both.
- 1D matrix (single row or column) — all cells reach both.

---

## 🎯 Interview Takeaways
- Reversing the flow direction (from ocean inward) avoids redundant computation.
- Two separate DFS traversals with intersection is cleaner than tracking both properties simultaneously.
- This "reverse reachability" technique applies to many grid-flow problems.

---

## 📌 Key Pattern
👉 **"Reverse DFS from boundaries — flow uphill from each ocean and intersect"**

---

## 🔁 Related Problems
- 130. Surrounded Regions
- 200. Number of Islands
- 407. Trapping Rain Water II

---

## 🚀 Final Thoughts
This problem beautifully demonstrates the reverse-flow technique. Instead of checking each cell individually, starting from the ocean boundaries and flowing uphill gives an efficient O(m*n) solution.

---

✨ **Rule to remember:**
> "When checking reachability to boundaries, start from the boundary and work inward."
