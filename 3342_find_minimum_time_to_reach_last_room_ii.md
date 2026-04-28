# 3342. Find Minimum Time to Reach Last Room II

## 🔗 Problem Link
https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Graph, Shortest Path, Dijkstra, Matrix, Heap (Priority Queue)

---

## 🧩 Problem Summary
Similar to 3341, but the movement cost alternates: odd-numbered moves cost 1 second, even-numbered moves cost 2 seconds (or vice versa based on position parity). Find the minimum time to reach `(m-1, n-1)` from `(0, 0)`.

### 📌 Constraints
- `2 <= m, n <= 750`
- `0 <= moveTime[i][j] <= 10^9`

---

## 💭 Intuition
👉 Same Dijkstra approach as 3341, but the move cost depends on the parity of `(i + j)`. From cell `(i, j)`, the cost is `(i + j) % 2 + 1`, alternating between 1 and 2.

---

## ⚡ Approach — Dijkstra with Alternating Move Costs

### 🧠 Idea
- Same structure as 3341.
- The only change: `newDist = max(moveTime[x][y], d) + ((i + j) % 2 + 1)`.
- The parity of the source cell `(i, j)` determines if the move costs 1 or 2.

---

## 💻 Code

```cpp
class Solution {
 public:
  // Similar to 3341. Find Minimum Time to Reach Last Room I
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
    using T = pair<int, pair<int, int>>;  // (d, (ux, uy))
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
        const int newDist = max(moveTime[x][y], d) + ((i + j) % 2 + 1);
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
Process (0,0): (i+j)%2+1 = 1
  (0,1) → max(4,0)+1=5, (1,0) → max(4,0)+1=5
Process (0,1): (i+j)%2+1 = 2
  (1,1) → max(4,5)+2=7
Process (1,0): (i+j)%2+1 = 2
  (1,1) → max(4,5)+2=7 (no improvement)
Result: 7
```

---

## ⏱️ Time Complexity
```
O(m * n * log(m * n)) — Dijkstra with priority queue
```

## 💾 Space Complexity
```
O(m * n)
```

---

## ⚠️ Edge Cases
- Grid size up to 750x750 → needs efficient Dijkstra
- Alternating costs mean path choice matters more than in version I
- Parity of starting position (0,0) always gives `(0+0)%2+1 = 1`

---

## 🎯 Interview Takeaways
- Position-dependent costs are handled naturally by Dijkstra — just change the weight formula.
- Parity-based cost is a common variation in grid shortest path problems.

---

## 📌 Key Pattern
👉 **"Dijkstra with position-dependent alternating edge weights"**

---

## 🔁 Related Problems
- 3341. Find Minimum Time to Reach Last Room I
- 1631. Path With Minimum Effort
- 2290. Minimum Obstacle Removal to Reach Corner

---

## 🚀 Final Thoughts
A minimal modification to 3341 — the only difference is `((i + j) % 2 + 1)` instead of a constant `1`. This shows how Dijkstra elegantly handles varying edge weights.

---

✨ **Rule to remember:**
> "Alternating costs in grids can be modeled by cell-coordinate parity."
