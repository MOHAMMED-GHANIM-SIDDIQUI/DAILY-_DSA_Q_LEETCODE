# 778. Swim in Rising Water

## 🔗 Problem Link
https://leetcode.com/problems/swim-in-rising-water/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Binary Search, Depth-First Search, Breadth-First Search, Union Find, Heap (Priority Queue), Matrix

---

## 🧩 Problem Summary
You are given an `n x n` grid where `grid[i][j]` represents the elevation at position `(i, j)`. At time `t`, you can swim to any adjacent cell if the elevation of both cells is at most `t`. Find the minimum time to swim from `(0, 0)` to `(n-1, n-1)`.

### 📌 Constraints
- `n == grid.length == grid[i].length`
- `1 <= n <= 50`
- `0 <= grid[i][j] < n^2`
- Each value in `grid` is unique.

---

## 💭 Intuition
👉 This is a shortest-path problem where the "cost" is the maximum elevation along the path. Using a min-heap (Dijkstra-like approach), we always expand the cell with the smallest elevation, tracking the maximum elevation seen so far.

---

## ⚡ Approach — Modified Dijkstra with Min-Heap

### 🧠 Idea
- Use a min-heap to always process the cell with the smallest elevation next.
- Track the maximum elevation encountered along the path from `(0,0)`.
- When we reach `(n-1, n-1)`, the tracked maximum is the answer.
- Mark cells as visited to avoid revisiting.

---

## 💻 Code

```cpp
class Solution {
 public:
  int swimInWater(vector<vector<int>>& grid) {
    constexpr int kDirs[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    const int n = grid.size();
    int ans = grid[0][0];
    using T = tuple<int, int, int>;  // (grid[i][j], i, j)
    priority_queue<T, vector<T>, greater<>> minHeap;
    vector<vector<bool>> seen(n, vector<bool>(n));

    minHeap.emplace(grid[0][0], 0, 0);
    seen[0][0] = true;

    while (!minHeap.empty()) {
      const auto [height, i, j] = minHeap.top();
      minHeap.pop();
      ans = max(ans, height);
      if (i == n - 1 && j == n - 1)
        break;
      for (const auto& [dx, dy] : kDirs) {
        const int x = i + dx;
        const int y = j + dy;
        if (x < 0 || x == n || y < 0 || y == n)
          continue;
        if (seen[x][y])
          continue;
        minHeap.emplace(grid[x][y], x, y);
        seen[x][y] = true;
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
grid = [[0,2],[1,3]]
```
### Steps
```
Start: heap = {(0,0,0)}, ans = 0
Pop (0,0,0): ans = max(0,0) = 0. Push neighbors (2,0,1) and (1,1,0)
Pop (1,1,0): ans = max(0,1) = 1. Push neighbor (3,1,1)
Pop (2,0,1): ans = max(1,2) = 2. (1,1) already via (3,1,1)
Pop (3,1,1): ans = max(2,3) = 3. Reached (1,1) -> return 3
```

---

## ⏱️ Time Complexity
```
O(n^2 log n), where n is the grid dimension (each cell pushed/popped from heap once)
```

## 💾 Space Complexity
```
O(n^2) for the heap and visited matrix
```

---

## ⚠️ Edge Cases
- 1x1 grid: return `grid[0][0]`.
- Grid where the path goes through the highest elevation cell.

---

## 🎯 Interview Takeaways
- Modified Dijkstra works great for "minimize the maximum edge" problems.
- Min-heap ensures we always explore the least-cost option first.
- This pattern appears in many grid pathfinding problems.

---

## 📌 Key Pattern
👉 **"Dijkstra-like min-heap traversal to minimize the maximum value along a path"**

---

## 🔁 Related Problems
- 1631. Path With Minimum Effort
- 787. Cheapest Flights Within K Stops
- 1102. Path With Maximum Minimum Value

---

## 🚀 Final Thoughts
This problem is a classic example of adapting Dijkstra's algorithm. Instead of summing edge weights, we track the maximum. The min-heap guarantees that we explore paths with the smallest bottleneck first, leading to an optimal solution.

---

✨ **Rule to remember:**
> "When you need to minimize the maximum cost along any path, think Dijkstra with a min-heap tracking the bottleneck."
