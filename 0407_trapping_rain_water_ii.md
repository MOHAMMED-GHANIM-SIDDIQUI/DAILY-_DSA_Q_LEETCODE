# 407. Trapping Rain Water II

## 🔗 Problem Link
https://leetcode.com/problems/trapping-rain-water-ii/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Breadth-First Search, Heap (Priority Queue), Matrix

---

## 🧩 Problem Summary
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, compute how much water it can trap after raining. Water flows in all four cardinal directions.

### 📌 Constraints
- `m == heightMap.length`
- `n == heightMap[i].length`
- `1 <= m, n <= 200`
- `0 <= heightMap[i][j] <= 2 * 10^4`

---

## 💭 Intuition
👉 Water level at any cell is determined by the minimum boundary height surrounding it. Process cells from the boundary inward using a min-heap, always expanding from the lowest boundary first.

---

## ⚡ Approach — BFS with Min-Heap (Priority Queue)

### 🧠 Idea
- Push all boundary cells into a min-heap.
- Process the lowest-height cell first. For each unvisited neighbor:
  - If the neighbor is lower, water fills to the current height (add the difference to answer).
  - Push the neighbor with `max(its height, current height)` into the heap.
- This ensures we always process from the lowest boundary inward.

---

## 💻 Code

```cpp
struct T {
  int i;
  int j;
  int h;  // heightMap[i][j] or the height after filling water
};

class Solution {
 public:
  int trapRainWater(vector<vector<int>>& heightMap) {
    constexpr int kDirs[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    const int m = heightMap.size();
    const int n = heightMap[0].size();
    int ans = 0;
    auto compare = [](const T& a, const T& b) { return a.h > b.h; };
    priority_queue<T, vector<T>, decltype(compare)> minHeap(compare);
    vector<vector<bool>> seen(m, vector<bool>(n));

    for (int i = 0; i < m; ++i) {
      minHeap.emplace(i, 0, heightMap[i][0]);
      minHeap.emplace(i, n - 1, heightMap[i][n - 1]);
      seen[i][0] = true;
      seen[i][n - 1] = true;
    }

    for (int j = 1; j < n - 1; ++j) {
      minHeap.emplace(0, j, heightMap[0][j]);
      minHeap.emplace(m - 1, j, heightMap[m - 1][j]);
      seen[0][j] = true;
      seen[m - 1][j] = true;
    }

    while (!minHeap.empty()) {
      const auto [i, j, h] = minHeap.top();
      minHeap.pop();
      for (const auto& [dx, dy] : kDirs) {
        const int x = i + dx;
        const int y = j + dy;
        if (x < 0 || x == m || y < 0 || y == n)
          continue;
        if (seen[x][y])
          continue;
        if (heightMap[x][y] < h) {
          ans += h - heightMap[x][y];
          minHeap.emplace(x, y, h);  // Fill water in grid[x][y].
        } else {
          minHeap.emplace(x, y, heightMap[x][y]);
        }
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
heightMap = [[1,4,3,1,3,2],
             [3,2,1,3,2,4],
             [2,3,3,2,3,1]]
```
### Steps
```
1. Push all boundary cells into min-heap, mark as seen.
2. Pop (2,2,1) [lowest boundary-adjacent cell after processing]:
   - Neighbor (1,2) has height 1, boundary h=1, no water trapped.
3. Continue popping lowest cells, filling water where interior < boundary.
4. Total water trapped: 4
```

---

## ⏱️ Time Complexity
```
O(m * n * log(m * n)) — each cell is pushed/popped from the heap once
```

## 💾 Space Complexity
```
O(m * n) — for the heap and seen matrix
```

---

## ⚠️ Edge Cases
- All boundary cells are higher than interior — maximum trapping.
- Flat surface — no water trapped.
- Matrix too small (m <= 2 or n <= 2) — no interior cells, no water.
- All cells same height — no water trapped.

---

## 🎯 Interview Takeaways
- This is the 2D generalization of the classic Trapping Rain Water problem.
- Min-heap BFS from boundary inward is the key technique.
- The water level at each cell is determined by the minimum path from it to the boundary.

---

## 📌 Key Pattern
👉 **"Min-heap BFS from boundary inward — water level equals the minimum surrounding boundary"**

---

## 🔁 Related Problems
- 42. Trapping Rain Water (1D version)
- 417. Pacific Atlantic Water Flow

---

## 🚀 Final Thoughts
This is one of the most elegant applications of priority-queue BFS. The insight that water can only be trapped relative to the lowest surrounding boundary, and processing from lowest to highest, makes the algorithm both correct and efficient.

---

✨ **Rule to remember:**
> "Start from the lowest boundary and work inward — water is trapped by the weakest wall."
