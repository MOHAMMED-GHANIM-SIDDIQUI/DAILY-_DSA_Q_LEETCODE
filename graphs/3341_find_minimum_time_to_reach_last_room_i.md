# 3341. Find Minimum Time to Reach Last Room I

## 🔗 Problem Link
https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Graph, Shortest Path, Dijkstra, Matrix, Heap (Priority Queue)

---

## 🧩 Problem Summary
Given a 2D grid `moveTime` where `moveTime[i][j]` is the earliest time you can start moving into cell `(i, j)`, find the minimum time to travel from `(0, 0)` to `(m-1, n-1)`. Each move takes 1 second, and you must wait if you arrive before the cell's `moveTime`.

### 📌 Constraints
- `2 <= m, n <= 50`
- `0 <= moveTime[i][j] <= 10^9`

---

## 💭 Intuition
👉 This is a shortest path problem with time-dependent edge weights. Use Dijkstra's algorithm where the cost to move to a neighbor is `max(moveTime[x][y], currentTime) + 1`.

---

## ⚡ Approach — Dijkstra's Algorithm

### 🧠 Idea
- Initialize `dist[0][0] = 0`, all others to `INT_MAX`.
- Use a min-heap of `(distance, position)`.
- For each neighbor, compute `newDist = max(moveTime[x][y], d) + 1`.
- Update if `newDist < dist[x][y]`.

---

## 💻 Code

```cpp
class Solution {
 public:
  int minTimeToReach(vector<vector<int>>& moveTime) {
    return dijkstra(moveTime, {0, 0},
                    {moveTime.size() - 1, moveTime[0].size() - 1});
  }

 private:
  int dijkstra(const vector<vector<int>>& moveTime, const pair<int, int>& src,
               const pair<int, int>& dst) {
    constexpr int kDirs[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    const int m = moveTime.size();
    const int n = moveTime[0].size();
    vector<vector<int>> dist(m, vector<int>(n, INT_MAX));

    dist[0][0] = 0;
    using T = pair<int, pair<int, int>>;  // (d, u)
    priority_queue<T, vector<T>, greater<>> minHeap;
    minHeap.push({dist[0][0], src});

    while (!minHeap.empty()) {
      const auto [d, u] = minHeap.top();
      minHeap.pop();
      if (u == dst)
        return d;
      const auto [i, j] = u;
      if (d > dist[i][j])
        continue;
      for (const auto& [dx, dy] : kDirs) {
        const int x = i + dx;
        const int y = j + dy;
        if (x < 0 || x == m || y < 0 || y == n)
          continue;
        const int newDist = max(moveTime[x][y], d) + 1;
        if (newDist < dist[x][y]) {
          dist[x][y] = newDist;
          minHeap.push({newDist, {x, y}});
        }
      }
    }

    return -1;
  }
};
```

---

## 🧠 Dry Run
### Input
```
moveTime = [[0, 4], [4, 4]]
```
### Steps
```
Start: dist[0][0] = 0
Process (0, 0): neighbors (0,1) → max(4,0)+1=5, (1,0) → max(4,0)+1=5
Process (0, 1) or (1, 0) with d=5:
  From (0,1): (1,1) → max(4,5)+1=6
  From (1,0): (1,1) → max(4,5)+1=6
Process (1,1) with d=6 → return 6
```

---

## ⏱️ Time Complexity
```
O(m * n * log(m * n)) — Dijkstra with a priority queue
```

## 💾 Space Complexity
```
O(m * n) — distance matrix and priority queue
```

---

## ⚠️ Edge Cases
- `moveTime[0][0]` is irrelevant (we start there at time 0)
- All zeros → standard BFS shortest path
- Very large `moveTime` values → lots of waiting

---

## 🎯 Interview Takeaways
- When movement cost depends on arrival time, Dijkstra handles it naturally.
- The `max(moveTime, currentTime) + moveCost` pattern models "wait then move."

---

## 📌 Key Pattern
👉 **"Dijkstra with time-dependent edge weights for grid shortest path"**

---

## 🔁 Related Problems
- 3342. Find Minimum Time to Reach Last Room II
- 787. Cheapest Flights Within K Stops
- 1631. Path With Minimum Effort

---

## 🚀 Final Thoughts
A clean application of Dijkstra to a grid problem with time-dependent constraints. The key formula `max(moveTime, d) + 1` captures the waiting behavior elegantly.

---

✨ **Rule to remember:**
> "When you must wait before entering a cell, use max(required_time, arrival_time) + travel_cost."
