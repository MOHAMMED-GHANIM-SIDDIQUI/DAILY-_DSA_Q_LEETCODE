# 2685. Count the Number of Complete Components

## 🔗 Problem Link
https://leetcode.com/problems/count-the-number-of-complete-components/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Graph, Union Find, Depth-First Search

---

## 🧩 Problem Summary
Given `n` vertices and an edge list, count the number of connected components that are complete (every pair of vertices in the component is directly connected by an edge). A complete component with `v` vertices must have exactly `v*(v-1)/2` edges.

### 📌 Constraints
- `1 <= n <= 50`
- `0 <= edges.length <= n * (n - 1) / 2`
- No self-loops or duplicate edges

---

## 💭 Intuition
👉 Use Union-Find to group vertices into connected components while tracking both node count and edge count per component. A component is complete if its edge count equals `nodeCount * (nodeCount - 1) / 2`.

---

## ⚡ Approach — Union-Find with Edge Counting

### 🧠 Idea
- Build a Union-Find that tracks `nodeCount` and `edgeCount` per component.
- For each edge, union the two nodes and increment the edge count.
- After processing all edges, check each unique root: if `edgeCount == nodeCount * (nodeCount - 1) / 2`, the component is complete.

---

## 💻 Code

```cpp
class UnionFind {
 public:
  UnionFind(int n) : id(n), rank(n), nodeCount(n, 1), edgeCount(n) {
    iota(id.begin(), id.end(), 0);
  }

  void unionByRank(int u, int v) {
    const int i = find(u);
    const int j = find(v);
    ++edgeCount[i];
    if (i == j)
      return;
    if (rank[i] < rank[j]) {
      id[i] = j;
      edgeCount[j] += edgeCount[i];
      nodeCount[j] += nodeCount[i];
    } else if (rank[i] > rank[j]) {
      id[j] = i;
      edgeCount[i] += edgeCount[j];
      nodeCount[i] += nodeCount[j];
    } else {
      id[i] = j;
      edgeCount[j] += edgeCount[i];
      nodeCount[j] += nodeCount[i];
      ++rank[j];
    }
  }

  int find(int u) {
    return id[u] == u ? u : id[u] = find(id[u]);
  }

  bool isComplete(int u) {
    return nodeCount[u] * (nodeCount[u] - 1) / 2 == edgeCount[u];
  }

 private:
  vector<int> id;
  vector<int> rank;
  vector<int> nodeCount;
  vector<int> edgeCount;
};

class Solution {
 public:
  int countCompleteComponents(int n, vector<vector<int>>& edges) {
    int ans = 0;
    UnionFind uf(n);
    unordered_set<int> parents;

    for (const vector<int>& edge : edges) {
      const int u = edge[0];
      const int v = edge[1];
      uf.unionByRank(u, v);
    }

    for (int i = 0; i < n; ++i) {
      const int parent = uf.find(i);
      if (parents.insert(parent).second && uf.isComplete(parent))
        ++ans;
    }

    return ans;
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
```
### Steps
```
Union(0,1): component {0,1} nodes=2, edges=1
Union(0,2): component {0,1,2} nodes=3, edges=2+1=3
Union(1,2): same component, edges=3+1... wait, 1 and 2 already connected
  find(1)=root, find(2)=root, same root => edgeCount[root]++ => edges=4?

Actually: edge(0,1): edgeCount incremented at root. edge(0,2): union, merge counts. edge(1,2): same root, just increment edge.

Component {0,1,2}: nodes=3, edges=3 => 3*(3-1)/2=3 ✓ Complete!
Component {3,4}: nodes=2, edges=1 => 2*(2-1)/2=1 ✓ Complete!
Node 5: nodes=1, edges=0 => 1*0/2=0 ✓ Complete!

Answer: 3
```

---

## ⏱️ Time Complexity
```
O(n + E * α(n)) where E is number of edges, α is inverse Ackermann
```

## 💾 Space Complexity
```
O(n)
```

---

## ⚠️ Edge Cases
- Isolated nodes (no edges) — each is a complete component of size 1
- Single connected component that is complete (a clique)
- A tree (connected but not complete unless n <= 2)

---

## 🎯 Interview Takeaways
- Union-Find can be augmented with extra data (edge count, node count) to answer richer queries.
- A connected component is complete iff edges == nodes*(nodes-1)/2.

---

## 📌 Key Pattern
👉 **"Augmented Union-Find — track extra metadata (edges, nodes) per component"**

---

## 🔁 Related Problems
- 323. Number of Connected Components in an Undirected Graph
- 547. Number of Provinces
- 1319. Number of Operations to Make Network Connected

---

## 🚀 Final Thoughts
This problem showcases the versatility of Union-Find. By tracking edge and node counts per component, we can efficiently determine completeness without needing adjacency lists or DFS traversals.

---

✨ **Rule to remember:**
> A connected component with v nodes is complete if and only if it has exactly v*(v-1)/2 edges.
