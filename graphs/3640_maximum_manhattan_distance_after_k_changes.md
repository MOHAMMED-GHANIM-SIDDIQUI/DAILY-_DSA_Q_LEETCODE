# 3640. Maximum Manhattan Distance After K Changes

## 🔗 Problem Link
https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Graph, Shortest Path, Dijkstra

---

## 🧩 Problem Summary
Given `n` nodes and directed weighted edges, find the minimum cost to travel from node 0 to node n-1. Forward edges have weight `w`, but traversing an edge in reverse costs `2w`. Use Dijkstra's algorithm on the modified graph.

### 📌 Constraints
- `2 <= n <= 10^5`
- `0 <= edges.length <= 2 * 10^5`
- Edge weights are positive integers

---

## 💭 Intuition
👉 Model the problem as a weighted directed graph where forward direction has cost `w` and reverse direction has cost `2w`, then run Dijkstra from source to find the shortest path.

---

## ⚡ Approach — Dijkstra with Asymmetric Edge Weights

### 🧠 Idea
- Build an adjacency list: for edge `(u, v, w)`, add `u→v` with weight `w` and `v→u` with weight `2w`.
- Run Dijkstra's algorithm from node 0.
- Return `dist[n-1]` or -1 if unreachable.

---

## 💻 Code

```python
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # Build graph
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, 2 * w))

        # Dijkstra setup
        dist = [float('inf')] * n
        dist[0] = 0
        visited = [False] * n
        heap = [(0, 0)]  # (distance, node)

        while heap:
            d, u = heapq.heappop(heap)

            if u == n - 1:
                return d

            if visited[u]:
                continue

            visited[u] = True

            for v, weight in g[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(heap, (dist[v], v))

        return -1
```

---

## 🧠 Dry Run
### Input
```
n = 3, edges = [[0, 1, 5], [1, 2, 3]]
```
### Steps
```
Graph:
  0 → [(1, 5)]
  1 → [(0, 10), (2, 3)]
  2 → [(1, 6)]

Dijkstra from 0:
  heap = [(0, 0)]
  Pop (0, 0): visit 0, push (5, 1)
  Pop (5, 1): visit 1, push (8, 2), push (15, 0)
  Pop (8, 2): node 2 == n-1 → return 8

Result: 8
```

---

## ⏱️ Time Complexity
```
O((V + E) log V) — standard Dijkstra with binary heap
```

## 💾 Space Complexity
```
O(V + E) — for the adjacency list and distance array
```

---

## ⚠️ Edge Cases
- No path exists from 0 to n-1 → return -1
- Direct edge from 0 to n-1
- All edges must be traversed in reverse
- Self-loops (if allowed)

---

## 🎯 Interview Takeaways
- Asymmetric edge weights (different cost for forward vs reverse) are handled naturally by Dijkstra.
- Early termination when destination is popped is a nice optimization.
- Always check if the destination is reachable.

---

## 📌 Key Pattern
👉 **"Model direction-dependent costs as asymmetric edge weights, then run standard Dijkstra."**

---

## 🔁 Related Problems
- 743. Network Delay Time
- 787. Cheapest Flights Within K Stops
- 1514. Path with Maximum Probability

---

## 🚀 Final Thoughts
This is a clean Dijkstra application with the twist of asymmetric edge weights. The key modeling insight is that reversing an edge doubles its cost, which naturally fits into a weighted directed graph.

---

✨ **Rule to remember:**
> "When edge costs depend on traversal direction, model as a directed graph with different weights per direction and run Dijkstra."
