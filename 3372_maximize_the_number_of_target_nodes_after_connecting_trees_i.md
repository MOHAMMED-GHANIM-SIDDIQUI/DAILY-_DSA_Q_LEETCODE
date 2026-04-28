# 3372. Maximize the Number of Target Nodes After Connecting Trees I

## 🔗 Problem Link
https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Tree, DFS, Graph

---

## 🧩 Problem Summary
Given two trees (as edge lists) and an integer `k`, for each node in Tree1, find the maximum number of "target nodes" — nodes reachable within distance `k` in Tree1 plus the maximum reachable within distance `k-1` from any node in Tree2 (since connecting requires 1 edge).

### 📌 Constraints
- `2 <= n, m <= 1000`
- `edges1.length == n - 1`, `edges2.length == m - 1`
- `0 <= k <= 1000`

---

## 💭 Intuition
👉 If we connect node `i` from Tree1 to some node `j` in Tree2, the connection uses 1 edge, leaving `k-1` edges to reach nodes in Tree2. To maximize, pick the node `j` in Tree2 that reaches the most nodes within `k-1`. This is independent of `i`, so precompute it once.

---

## ⚡ Approach — DFS for Reachable Nodes + Greedy Connection

### 🧠 Idea
- For each node in Tree2, compute nodes reachable within depth `k-1` using DFS. Take the maximum.
- For each node in Tree1, compute nodes reachable within depth `k` using DFS.
- Result for node `i` = reachableInTree1[i] + maxReachableInTree2.

---

## 💻 Code

```cpp
class Solution {
public:
    std::vector<int> maxTargetNodes(std::vector<std::vector<int>>& edges1,
                                    std::vector<std::vector<int>>& edges2, int k) {
        int n = edges1.size() + 1;
        int m = edges2.size() + 1;

        // Build adjacency lists for both trees
        std::vector<std::vector<int>> tree1 = buildGraph(edges1, n);
        std::vector<std::vector<int>> tree2 = buildGraph(edges2, m);

        // Compute maximum reachable nodes in Tree2 within depth k - 1
        int maxReachTree2 = 0;
        if (k > 0) {
            for (int i = 0; i < m; ++i) {
                maxReachTree2 = std::max(maxReachTree2, dfs(tree2, i, -1, k - 1));
            }
        }

        // Compute result for each node in Tree1
        std::vector<int> result;
        for (int i = 0; i < n; ++i) {
            int reachTree1 = dfs(tree1, i, -1, k);
            result.push_back(reachTree1 + maxReachTree2);
        }

        return result;
    }

private:
    // Helper function to build adjacency list from edge list
    std::vector<std::vector<int>> buildGraph(const std::vector<std::vector<int>>& edges, int size) {
        std::vector<std::vector<int>> graph(size);
        for (const auto& edge : edges) {
            int u = edge[0], v = edge[1];
            graph[u].push_back(v);
            graph[v].push_back(u);
        }
        return graph;
    }

    // DFS to count nodes reachable within depth k
    int dfs(const std::vector<std::vector<int>>& graph, int node, int parent, int k) {
        if (k < 0) return 0;
        int count = 1; // Count the current node
        for (int neighbor : graph[node]) {
            if (neighbor != parent) {
                count += dfs(graph, neighbor, node, k - 1);
            }
        }
        return count;
    }
};
```

---

## 🧠 Dry Run
### Input
```
edges1 = [[0,1],[0,2]], edges2 = [[0,1]], k = 2
```
### Steps
```
Tree1: 0-1, 0-2 (star with center 0)
Tree2: 0-1

maxReachTree2 (k-1=1):
  node 0: dfs depth 1 → count 2 (0, 1)
  node 1: dfs depth 1 → count 2 (1, 0)
  maxReachTree2 = 2

For Tree1 (k=2):
  node 0: dfs depth 2 → 3 (0, 1, 2)
  node 1: dfs depth 2 → 3 (1, 0, 2)
  node 2: dfs depth 2 → 3 (2, 0, 1)

Result: [3+2, 3+2, 3+2] = [5, 5, 5]
```

---

## ⏱️ Time Complexity
```
O(n^2 + m^2) — DFS from each node in both trees
```

## 💾 Space Complexity
```
O(n + m) — adjacency lists and recursion stack
```

---

## ⚠️ Edge Cases
- `k = 0` → only the node itself is reachable, no connection benefit
- `k = 1` → only immediate neighbors in Tree1, no Tree2 benefit
- Small trees (n=2 or m=2) → limited reachability

---

## 🎯 Interview Takeaways
- Decoupling the two trees simplifies the problem: Tree2's contribution is a single precomputed maximum.
- DFS with depth limit is a clean way to count reachable nodes.

---

## 📌 Key Pattern
👉 **"Precompute best connection point independently, then combine with per-node DFS"**

---

## 🔁 Related Problems
- 3373. Maximize the Number of Target Nodes After Connecting Trees II
- 863. All Nodes Distance K in Binary Tree
- 834. Sum of Distances in Tree

---

## 🚀 Final Thoughts
The key insight is that the optimal connection to Tree2 is independent of which Tree1 node we're evaluating. This decoupling reduces the problem to two independent DFS computations plus a simple addition.

---

✨ **Rule to remember:**
> "When connecting trees, the best connection point in the other tree is independent of the source — precompute it once."
