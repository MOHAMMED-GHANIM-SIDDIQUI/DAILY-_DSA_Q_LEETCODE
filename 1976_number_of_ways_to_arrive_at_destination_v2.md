# 1976. Number of Ways to Arrive at Destination

## 🔗 Problem Link
https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Graph, Dijkstra's Algorithm, Shortest Path, Dynamic Programming

---

## 🧩 Problem Summary
You are in a city with `n` intersections numbered from `0` to `n - 1` with bi-directional roads. Given the roads and their travel times, find the number of ways to travel from intersection `0` to intersection `n - 1` in the shortest amount of time. Return the answer modulo 10^9 + 7.

### 📌 Constraints
- `1 <= n <= 200`
- `n - 1 <= roads.length <= n * (n - 1) / 2`
- `roads[i].length == 3`
- `0 <= u_i, v_i <= n - 1`
- `1 <= time_i <= 10^9`
- No duplicate edges, no self-loops

---

## 💭 Intuition
👉 Run Dijkstra's shortest path algorithm while simultaneously counting the number of distinct shortest paths to each node. When a shorter path is found, reset the count; when an equal-length path is found, add the counts.

---

## ⚡ Approach — Dijkstra with Path Counting

### 🧠 Idea
- Build an adjacency list from the roads.
- Use Dijkstra's algorithm with a min-heap.
- Maintain a `ways[]` array: `ways[v]` = number of shortest paths to node `v`.
- When relaxing edge `(u, v)`: if `dist[u] + w < dist[v]`, update dist and set `ways[v] = ways[u]`; if equal, add `ways[u]` to `ways[v]`.
- Return `ways[n-1]`.

---

## 💻 Code

```cpp
class Solution {
 public:
  int countPaths(int n, vector<vector<int>>& roads) {
    // Step 1: Build the graph representation
    vector<vector<pair<int, int>>> graph(n);

    for (const vector<int>& road : roads) {
      int u = road[0];
      int v = road[1];
      int w = road[2];
      graph[u].emplace_back(v, w);
      graph[v].emplace_back(u, w);
    }

    // Step 2: Run Dijkstra to find the number of distinct shortest paths
    return dijkstra(graph, 0, n - 1);
  }

 private:
  // Dijkstra algorithm to find the number of distinct shortest paths from src to dst
  int dijkstra(const vector<vector<pair<int, int>>>& graph, int src, int dst) {
    constexpr int MOD = 1'000'000'007;

    // Number of ways to reach each node
    vector<long> ways(graph.size(), 0);

    // Distance array initialized to a very large number (infinity)
    vector<long> dist(graph.size(), LONG_MAX);

    ways[src] = 1;  // There's 1 way to be at the source (start point)
    dist[src] = 0;  // Distance to source is 0

    // Priority queue for Dijkstra (min-heap)
    using P = pair<long, int>;  // (distance, node)
    priority_queue<P, vector<P>, greater<>> minHeap;
    minHeap.emplace(0, src);

    while (!minHeap.empty()) {
      auto [d, u] = minHeap.top();
      minHeap.pop();

      if (d > dist[u]) continue;  // Skip if this is not the shortest path to u

      // Iterate over neighbors
      for (const auto& [v, w] : graph[u]) {
        // If a shorter path to v is found
        if (d + w < dist[v]) {
          dist[v] = d + w;
          ways[v] = ways[u];  // Set the number of ways to reach v as the number of ways to reach u
          minHeap.emplace(dist[v], v);
        }
        // If an equal length path to v is found, add the number of ways to reach u to v
        else if (d + w == dist[v]) {
          ways[v] = (ways[v] + ways[u]) % MOD;
        }
      }
    }

    // Return the number of ways to reach the destination (dst)
    return ways[dst];
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
```
### Steps
```
Dijkstra from node 0:
dist[0]=0, ways[0]=1
Process 0: update dist[6]=7(ways=1), dist[1]=2(ways=1), dist[4]=5(ways=1)
Process 1: update dist[2]=5(ways=1), dist[3]=5(ways=1)
Process 4: update dist[6]=7(ways=1+1=2, equal path found)
Process 2: update dist[5]=6(ways=1)
Process 3: update dist[5]=6(ways=1+1=2, equal), dist[6]=8(not shorter)
Process 5: update dist[6]=7(ways=2+2=4, equal)
Result: ways[6] = 4
```

---

## ⏱️ Time Complexity
```
O((V + E) log V), where V = n nodes and E = number of roads
```

## 💾 Space Complexity
```
O(V + E) for the graph, distance, and ways arrays
```

---

## ⚠️ Edge Cases
- Only two nodes with one road: exactly 1 way
- Multiple equal-weight paths: counts accumulate correctly
- Large edge weights: use `long` to avoid overflow
- Single node (n=1): return 1

---

## 🎯 Interview Takeaways
- Dijkstra can be extended to count shortest paths by maintaining a parallel `ways[]` array.
- When a shorter path is found, reset the count; when an equal path is found, add counts.
- Use `long` types to avoid integer overflow with large weights.

---

## 📌 Key Pattern
👉 **"Dijkstra + path counting: reset on shorter, accumulate on equal"**

---

## 🔁 Related Problems
- 743. Network Delay Time
- 787. Cheapest Flights Within K Stops
- 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

---

## 🚀 Final Thoughts
This problem elegantly combines shortest path computation with combinatorial counting. The key insight is that Dijkstra naturally provides the framework for counting paths: just track how many ways you can reach each node with the current shortest distance.

---

✨ **Rule to remember:**
> In Dijkstra, when you find an equal-distance path, add the way counts; when shorter, replace them.
