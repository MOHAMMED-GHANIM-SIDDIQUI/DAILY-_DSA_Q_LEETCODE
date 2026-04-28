# 1857. Largest Color Value in a Directed Graph

## 🔗 Problem Link
https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Graph, Topological Sort, Dynamic Programming, BFS

---

## 🧩 Problem Summary
Given a directed graph where each node has a color (lowercase letter), find the largest color value of any valid path. The color value of a path is the maximum frequency of any single color along that path. Return -1 if the graph contains a cycle.

### 📌 Constraints
- `1 <= n <= 10^5`
- `0 <= m <= 10^5`
- `colors.length == n`
- `colors` consists of lowercase English letters

---

## 💭 Intuition
👉 Use topological sort (Kahn's algorithm) to process nodes in order. For each node, maintain a count array of 26 colors representing the maximum frequency of each color on any path ending at that node. If we cannot process all nodes, a cycle exists.

---

## ⚡ Approach — Topological Sort + DP on Color Counts

### 🧠 Idea
- Build the graph and compute in-degrees.
- Initialize a queue with all zero-in-degree nodes.
- For each node, maintain `count[node][c]` = max frequency of color `c` on any path ending at `node`.
- When processing a node, increment its own color count and propagate to neighbors.
- Track the global maximum color count as the answer.
- If the number of processed nodes is less than `n`, a cycle exists — return -1.

---

## 💻 Code

```cpp
class Solution {
 public:
  int largestPathValue(string colors, vector<vector<int>>& edges) {
    const int n = colors.length();
    int ans = 0;
    int processed = 0;
    vector<vector<int>> graph(n);
    vector<int> inDegrees(n);
    queue<int> q;
    vector<vector<int>> count(n, vector<int>(26));

    // Build the graph.
    for (const vector<int>& edge : edges) {
      const int u = edge[0];
      const int v = edge[1];
      graph[u].push_back(v);
      ++inDegrees[v];
    }

    // Perform topological sorting.
    for (int i = 0; i < n; ++i)
      if (inDegrees[i] == 0)
        q.push(i);

    while (!q.empty()) {
      const int out = q.front();
      q.pop();
      ++processed;
      ans = max(ans, ++count[out][colors[out] - 'a']);
      for (const int in : graph[out]) {
        for (int i = 0; i < 26; ++i)
          count[in][i] = max(count[in][i], count[out][i]);
        if (--inDegrees[in] == 0)
          q.push(in);
      }
    }

    return processed == n ? ans : -1;
  }
};
```

---

## 🧠 Dry Run
### Input
```
colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
```
### Steps
```
Graph: 0→1, 0→2, 2→3, 3→4
In-degrees: [0,1,1,1,1]
Queue starts: [0]

Process 0 (color 'a'): count[0][0]=1, ans=1
  Propagate to 1: count[1] = max(count[1], count[0])
  Propagate to 2: count[2] = max(count[2], count[0])
  Queue: [1, 2]

Process 1 (color 'b'): count[1][1]=1, ans=1
  No neighbors. Queue: [2]

Process 2 (color 'a'): count[2][0]=2, ans=2
  Propagate to 3. Queue: [3]

Process 3 (color 'c'): count[3][2]=1, ans=2
  Propagate to 4. Queue: [4]

Process 4 (color 'a'): count[4][0]=3, ans=3

processed=5 == n=5 → return 3
```

---

## ⏱️ Time Complexity
```
O(n * 26 + m), where n is the number of nodes and m is the number of edges
```

## 💾 Space Complexity
```
O(n * 26) for the color count table
```

---

## ⚠️ Edge Cases
- Graph has a cycle → return -1
- Single node with no edges → return 1
- All nodes have the same color → answer is the length of the longest path
- Disconnected graph → topological sort handles multiple components

---

## 🎯 Interview Takeaways
- Topological sort is essential for DAG-based DP problems.
- Cycle detection comes for free with Kahn's algorithm — just check if all nodes were processed.
- Propagating a fixed-size state (26 colors) along edges is a common DP-on-DAG pattern.

---

## 📌 Key Pattern
👉 **"Topological sort + DP to aggregate path properties in a DAG"**

---

## 🔁 Related Problems
- 207. Course Schedule
- 210. Course Schedule II
- 329. Longest Increasing Path in a Matrix
- 2050. Parallel Courses III

---

## 🚀 Final Thoughts
This problem elegantly combines topological sorting with dynamic programming. The key realization is that for each node, we only need to track 26 color frequencies, and these can be propagated through the DAG in topological order.

---

✨ **Rule to remember:**
> Topological sort + per-node DP state propagation solves most "optimal path in DAG" problems.
