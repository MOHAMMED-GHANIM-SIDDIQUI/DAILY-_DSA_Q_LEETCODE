# 3373. Maximize the Number of Target Nodes After Connecting Trees II

## 🔗 Problem Link
https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Tree, DFS, Graph, Bipartite / Parity

---

## 🧩 Problem Summary
Given two trees represented by edge lists, for each node in tree1, find the maximum number of target nodes reachable with even-length paths if you are allowed to connect one node from tree1 to one node in tree2. The target nodes are those reachable via an even number of edges from the given node.

### 📌 Constraints
- 2 <= n, m <= 10^5
- edges1.length == n - 1, edges2.length == m - 1
- Each edges[i] = [u, v] represents an undirected edge

---

## 💭 Intuition
👉 In a tree, all nodes can be divided into two groups based on parity (even/odd depth). A node can reach all same-parity nodes in even steps and opposite-parity nodes in odd steps. When connecting to tree2, you can pick whichever parity group in tree2 is larger.

---

## ⚡ Approach — Parity-Based DFS

### 🧠 Idea
- Build adjacency lists for both trees.
- DFS from root to assign parity (even/odd depth) to every node.
- Count even-parity and odd-parity nodes in both trees.
- For each node i in tree1, the count from tree1 is the number of same-parity nodes.
- From tree2, greedily pick max(even2, odd2) since you can connect to any node.
- Answer for node i = same-parity count in tree1 + max(even2, odd2).

---

## 💻 Code

```cpp
class Solution {
 public:
  vector<int> maxTargetNodes(vector<vector<int>>& edges1,
                             vector<vector<int>>& edges2) {
    const int n = edges1.size() + 1;
    const int m = edges2.size() + 1;
    vector<int> ans;
    const vector<vector<int>> graph1 = buildGraph(edges1);
    const vector<vector<int>> graph2 = buildGraph(edges2);
    vector<bool> parity1(n);
    vector<bool> parity2(m);  // placeholder (parity2 is not used)
    const int even1 = dfs(graph1, 0, -1, parity1, /*isEven=*/true);
    const int even2 = dfs(graph2, 0, -1, parity2, /*isEven=*/true);
    const int odd1 = n - even1;
    const int odd2 = m - even2;

    for (int i = 0; i < n; ++i) {
      const int tree1 = parity1[i] ? even1 : odd1;
      // Can connect the current node in tree1 to either an even node or an odd
      // node in tree2.
      const int tree2 = max(even2, odd2);
      ans.push_back(tree1 + tree2);
    }

    return ans;
  }

 private:
  // Returns the number of nodes that can be reached from u with even steps.
  int dfs(const vector<vector<int>>& graph, int u, int prev,
          vector<bool>& parity, bool isEven) {
    int res = isEven ? 1 : 0;
    parity[u] = isEven;
    for (const int v : graph[u])
      if (v != prev)
        res += dfs(graph, v, u, parity, !isEven);
    return res;
  }

  vector<vector<int>> buildGraph(const vector<vector<int>>& edges) {
    vector<vector<int>> graph(edges.size() + 1);
    for (const vector<int>& edge : edges) {
      const int u = edge[0];
      const int v = edge[1];
      graph[u].push_back(v);
      graph[v].push_back(u);
    }
    return graph;
  }
};
```

---

## 🧠 Dry Run
### Input
```
edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3]]
```
### Steps
```
Tree1: 0-1, 0-2, 2-3, 2-4
  Parity: 0(even), 1(odd), 2(odd), 3(even), 4(even)
  even1 = 3 (nodes 0,3,4), odd1 = 2 (nodes 1,2)

Tree2: 0-1, 0-2, 0-3
  Parity: 0(even), 1(odd), 2(odd), 3(odd)
  even2 = 1, odd2 = 3 => max = 3

Node 0 (even): 3 + 3 = 6
Node 1 (odd):  2 + 3 = 5
Node 2 (odd):  2 + 3 = 5
Node 3 (even): 3 + 3 = 6
Node 4 (even): 3 + 3 = 6
Result: [6, 5, 5, 6, 6]
```

---

## ⏱️ Time Complexity
```
O(n + m) — single DFS on each tree
```

## 💾 Space Complexity
```
O(n + m) — adjacency lists and parity arrays
```

---

## ⚠️ Edge Cases
- Trees with only 2 nodes (single edge)
- Star-shaped trees where all leaves share the same parity
- When even2 == odd2, either choice yields the same result

---

## 🎯 Interview Takeaways
- Trees are bipartite — parity of depth determines reachability via even/odd paths.
- When you can freely choose a connection point, greedily pick the larger group.
- Precomputing parity in a single DFS avoids per-node BFS.

---

## 📌 Key Pattern
👉 **"Tree bipartiteness / parity-based counting"**

---

## 🔁 Related Problems
- 3372. Maximize the Number of Target Nodes After Connecting Trees I
- 785. Is Graph Bipartite?
- 886. Possible Bipartition

---

## 🚀 Final Thoughts
This problem elegantly reduces to tree bipartiteness. By recognizing that even-step reachability splits into parity groups, the entire solution becomes a single DFS per tree plus a greedy max selection.

---

✨ **Rule to remember:**
> In a tree, nodes at even distance from a root share the same parity group — exploit bipartiteness for even/odd path counting.
