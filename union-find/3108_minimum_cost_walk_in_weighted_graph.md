# 3108. Minimum Cost Walk in Weighted Graph

## 🔗 Problem Link
https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Union Find, Graph, Bit Manipulation

---

## 🧩 Problem Summary
Given a weighted undirected graph, answer queries asking for the minimum cost walk between two nodes. The cost of a walk is the bitwise AND of all edge weights along the path. You may revisit nodes and edges. Return -1 if no path exists.

### 📌 Constraints
- 1 <= n <= 10^5
- 0 <= edges.length <= 10^5
- edges[i].length == 3
- 0 <= query.length <= 10^5

---

## 💭 Intuition
👉 Since you can traverse edges multiple times, the minimum AND cost within a connected component is simply the AND of ALL edge weights in that component (more edges means more bits get cleared). Use Union-Find to group nodes.

---

## ⚡ Approach — Union Find + Bitwise AND

### 🧠 Idea
- Build a Union-Find to identify connected components
- For each component, compute the AND of all edge weights
- For each query: if same node return 0, if same component return the component AND, otherwise -1

---

## 💻 Code

```cpp
class UnionFind {
public:
    UnionFind(int n) {
        p = vector<int>(n);
        size = vector<int>(n, 1);
        iota(p.begin(), p.end(), 0);
    }

    bool unite(int a, int b) {
        int pa = find(a), pb = find(b);
        if (pa == pb) {
            return false;
        }
        if (size[pa] > size[pb]) {
            p[pb] = pa;
            size[pa] += size[pb];
        } else {
            p[pa] = pb;
            size[pb] += size[pa];
        }
        return true;
    }

    int find(int x) {
        if (p[x] != x) {
            p[x] = find(p[x]);
        }
        return p[x];
    }

    int getSize(int x) {
        return size[find(x)];
    }

private:
    vector<int> p, size;
};

class Solution {
public:
    vector<int> minimumCost(int n, vector<vector<int>>& edges, vector<vector<int>>& query) {
        g = vector<int>(n, -1);
        uf = new UnionFind(n);
        for (auto& e : edges) {
            uf->unite(e[0], e[1]);
        }
        for (auto& e : edges) {
            int root = uf->find(e[0]);
            g[root] &= e[2];
        }
        vector<int> ans;
        for (auto& q : query) {
            ans.push_back(f(q[0], q[1]));
        }
        return ans;
    }

private:
    UnionFind* uf;
    vector<int> g;

    int f(int u, int v) {
        if (u == v) {
            return 0;
        }
        int a = uf->find(u), b = uf->find(v);
        return a == b ? g[a] : -1;
    }
};
```

---

## 🧠 Dry Run
### Input
```
n=5, edges=[[0,1,7],[1,3,7],[1,2,1]], query=[[0,3],[3,4]]
```
### Steps
```
Union: 0-1, 1-3, 1-2 -> component {0,1,2,3}, node 4 alone
AND of edges in component: 7 & 7 & 1 = 1
g[root] = 1 for that component, g[4] = -1 (init)
Query [0,3]: same component -> return 1
Query [3,4]: different components -> return -1
Result: [1, -1]
```

---

## ⏱️ Time Complexity
```
O((n + E + Q) * α(n)) — Union-Find with path compression, near-linear
```

## 💾 Space Complexity
```
O(n) — Union-Find and AND array
```

---

## ⚠️ Edge Cases
- Query where u == v: return 0
- Disconnected nodes: return -1
- Single edge component: AND is just that edge's weight

---

## 🎯 Interview Takeaways
- When you can traverse edges unlimited times, the AND of all edges in the component is the answer
- Initializing the AND array to -1 (all bits set) is the correct identity for AND
- Union-Find is the natural choice for connected component queries

---

## 📌 Key Pattern
👉 **"Union-Find + aggregate bitwise operation per connected component"**

---

## 🔁 Related Problems
- 1697. Checking Existence of Edge Length Limited Paths
- 1724. Checking Existence of Edge Length Limited Paths II
- 2492. Minimum Score of a Path Between Two Cities

---

## 🚀 Final Thoughts
The insight that revisiting edges only helps (AND can only decrease or stay the same) means the optimal walk uses all edges in the component. This collapses the problem to Union-Find with a per-component AND reduction.

---

✨ **Rule to remember:**
> In a walk with AND cost, you want MORE edges — AND all edges in each connected component.
