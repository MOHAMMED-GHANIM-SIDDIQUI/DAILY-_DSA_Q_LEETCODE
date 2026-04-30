# 2359. Find Closest Node to Given Two Nodes

## 🔗 Problem Link
https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Graph, Depth-First Search

---

## 🧩 Problem Summary
Given a directed graph where each node has at most one outgoing edge, and two starting nodes `node1` and `node2`, find the node that can be reached from both and minimizes the maximum of the two distances. If there are ties, return the smallest index.

### 📌 Constraints
- `n == edges.length`
- `2 <= n <= 10^5`
- `-1 <= edges[i] < n`
- `edges[i] != i`

---

## 💭 Intuition
👉 Since each node has at most one outgoing edge, the graph is a functional graph. Compute distances from both starting nodes by following edges, then find the node minimizing `max(dist1[i], dist2[i])`.

---

## ⚡ Approach — Two Distance Arrays

### 🧠 Idea
- Compute `dist1` and `dist2`: distance from `node1` and `node2` to every reachable node by following the single outgoing edges.
- For each node reachable from both, compute `max(dist1[i], dist2[i])`.
- Return the node with minimum such max-distance (smallest index on ties).

---

## 💻 Code

```cpp
class Solution {
 public:
  int closestMeetingNode(vector<int>& edges, int node1, int node2) {
    constexpr int kMax = 10000;
    const vector<int> dist1 = getDist(edges, node1);
    const vector<int> dist2 = getDist(edges, node2);
    int minDist = kMax;
    int ans = -1;

    for (int i = 0; i < edges.size(); ++i)
      if (min(dist1[i], dist2[i]) >= 0) {
        const int maxDist = max(dist1[i], dist2[i]);
        if (maxDist < minDist) {
          minDist = maxDist;
          ans = i;
        }
      }

    return ans;
  }

 private:
  vector<int> getDist(const vector<int>& edges, int u) {
    vector<int> dist(edges.size(), -1);
    int d = 0;
    while (u != -1 && dist[u] == -1) {
      dist[u] = d++;
      u = edges[u];
    }
    return dist;
  }
};
```

---

## 🧠 Dry Run
### Input
```
edges = [2,2,3,-1], node1 = 0, node2 = 1
```
### Steps
```
getDist(0): 0→0, 2→1, 3→2 → dist1 = [0,-1,1,2]
getDist(1): 1→0, 2→1, 3→2 → dist2 = [-1,0,1,2]

i=0: dist1=0, dist2=-1 → skip (not reachable from node2)
i=1: dist1=-1, dist2=0 → skip
i=2: dist1=1, dist2=1 → max=1 < 10000 → ans=2, minDist=1
i=3: dist1=2, dist2=2 → max=2 >= 1 → skip

Result: 2
```

---

## ⏱️ Time Complexity
```
O(n) — two traversals of at most n edges each, plus one scan.
```

## 💾 Space Complexity
```
O(n) — two distance arrays.
```

---

## ⚠️ Edge Cases
- No common reachable node: return -1.
- One node is on the path from the other.
- Cycles in the graph (handled by checking `dist[u] == -1`).

---

## 🎯 Interview Takeaways
- Functional graphs (out-degree ≤ 1) allow simple path traversal without BFS/DFS queues.
- Minimizing the maximum of two distances is a common "meeting point" pattern.
- Iterate in order to naturally break ties by smallest index.

---

## 📌 Key Pattern
👉 **"Compute distances from two sources in a functional graph, minimize max-distance at meeting point."**

---

## 🔁 Related Problems
- 2360. Longest Cycle in a Graph
- 997. Find the Town Judge
- 1971. Find if Path Exists in Graph

---

## 🚀 Final Thoughts
The functional graph structure makes distance computation trivially linear. The core challenge is formulating the optimization criterion correctly: minimize the maximum of the two distances.

---

✨ **Rule to remember:**
> "In functional graphs, follow edges to compute distances — then minimize the bottleneck."
