# 3559. Number of Ways to Assign Edge Weights II

## 🔗 Problem Link
https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Tree, Depth-First Search, Math, Binary Lifting (LCA)

---

## 🧩 Problem Summary

You are given a tree rooted at node `1`. Each edge can be assigned a weight of `1` or `2`. You are also given `queries`, where each query `[u, v]` asks for the number of weight assignments **along the path from `u` to `v`** whose total weight is **odd**, modulo `10^9 + 7`. Return an array with the answer for each query.

If the path has `d` edges, exactly half of the `2^d` assignments are odd, so the per-query answer is `2^(d-1)`. When `u == v` the path has no edges, so the answer is `0`.

### 📌 Constraints
- `2 <= n <= 10^5`
- `edges.length == n - 1`, forming a valid tree rooted at node `1`.
- `1 <= queries.length <= 10^5`
- `queries[i] = [u_i, v_i]` with `1 <= u_i, v_i <= n`.

---

## 💭 Intuition

👉 As in problem I, only the **number of edges `d` on the path** matters, and exactly half of the `2^d` assignments give an odd sum → `2^(d-1)`. For an arbitrary path `u → v` in a rooted tree, the edge count is `depth[u] + depth[v] - 2*depth[lca(u, v)]`. With many queries we need fast LCA, so we precompute a **binary-lifting (sparse) table** to answer each LCA in `O(log n)`.

---

## ⚡ Approach — Binary Lifting (LCA) + Power of Two

### 🧠 Idea
- Build an adjacency list and run a DFS from root `1` to record `depth[v]` and the immediate ancestor `up[0][v]` (the parent).
- Fill the sparse table: `up[k][v] = up[k-1][ up[k-1][v] ]`, the `2^k`-th ancestor of `v`, for `k` from `1` to `LOG-1`.
- **LCA(a, b):** lift the deeper node up by the depth difference (bit by bit); if they meet, that's the LCA. Otherwise lift both nodes up in lockstep from the highest power while their ancestors differ; the answer is the parent `up[0][a]`.
- For each query `[u, v]`:
  - If `u == v`: append `0` (no edges).
  - Else compute `w = lca(u, v)`, `d = depth[u] + depth[v] - 2*depth[w]`, and append `pow(2, d-1, MOD)`.

---

## 💻 Code

```python
class Solution:
    def assignEdgeWeights(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7

        n = len(edges) + 1
        LOG = (n + 1).bit_length()

        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        depth = [0] * (n + 1)
        up = [[0] * (n + 1) for _ in range(LOG)]

        def dfs(u: int, p: int):
            up[0][u] = p
            for v in g[u]:
                if v != p:
                    depth[v] = depth[u] + 1
                    dfs(v, u)

        dfs(1, 0)

        for k in range(1, LOG):
            for v in range(1, n + 1):
                up[k][v] = up[k - 1][up[k - 1][v]]

        def lca(a: int, b: int) -> int:
            if depth[a] < depth[b]:
                a, b = b, a

            diff = depth[a] - depth[b]
            for k in range(LOG):
                if diff & (1 << k):
                    a = up[k][a]

            if a == b:
                return a

            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a = up[k][a]
                    b = up[k][b]

            return up[0][a]

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            w = lca(u, v)
            d = depth[u] + depth[v] - 2 * depth[w]

            ans.append(pow(2, d - 1, MOD))

        return ans
```

---

## 🧠 Dry Run

### Input
```
edges = [[1,2],[1,3],[3,4],[3,5]]
queries = [[4,5],[2,4],[3,3]]
n = 5, LOG = bit_length(6) = 3
```

### Steps
```
Adjacency:
  1: [2,3]   2: [1]   3: [1,4,5]   4: [3]   5: [3]

DFS from (1,0):
  depth: 1->0, 2->1, 3->1, 4->2, 5->2
  up[0]: 1->0, 2->1, 3->1, 4->3, 5->3

Sparse table up[k][v] = up[k-1][up[k-1][v]]:
  up[1]: ancestor 2 levels up
    up[1][2]=up[0][up[0][2]]=up[0][1]=0
    up[1][3]=up[0][1]=0
    up[1][4]=up[0][up[0][4]]=up[0][3]=1
    up[1][5]=up[0][3]=1
  up[2]: all resolve to 0 for these nodes

Query [4,5]:
  u!=v. lca(4,5): depth equal (2,2), diff=0.
    a=4,b=5, not equal. k from high:
      k=1: up[1][4]=1, up[1][5]=1 -> equal, skip
      k=0: up[0][4]=3, up[0][5]=3 -> equal, skip
    return up[0][4]=3 -> w=3
  d = 2 + 2 - 2*1 = 2 -> 2^(2-1)=2

Query [2,4]:
  lca(2,4): depth[2]=1 < depth[4]=2 -> swap a=4,b=2
    diff = 2-1 = 1 -> bit0 set: a=up[0][4]=3 (now depth 1)
    a=3, b=2, not equal. k high:
      k=1: up[1][3]=0, up[1][2]=0 -> equal, skip
      k=0: up[0][3]=1, up[0][2]=1 -> equal, skip
    return up[0][3]=1 -> w=1
  d = depth[2]+depth[4]-2*depth[1] = 1+2-0 = 3 -> 2^(3-1)=4

Query [3,3]:
  u==v -> append 0

ans = [2, 4, 0]
```

---

## ⏱️ Time Complexity
```
O((n + q) log n)
```
Building the sparse table is `O(n log n)`. The DFS is `O(n)`. Each of the `q` queries does an `O(log n)` LCA plus an `O(log d)` modular power, giving `O(q log n)` overall.

---

## 💾 Space Complexity
```
O(n log n)
```
The binary-lifting table `up` has `LOG` rows of `n + 1` entries each. The adjacency list and `depth` array add `O(n)`, and the recursive DFS stack can reach `O(n)` on a skewed tree.

---

## ⚠️ Edge Cases
- **`u == v`:** path has zero edges, answer `0` (also avoids `2^(-1)`).
- **One node is an ancestor of the other:** the LCA equals the shallower node; the lockstep loop returns early after the depth-equalizing lift.
- **Skewed (path-like) tree:** DFS recursion depth can reach `n`; for very large `n`, recursion limits may need raising, but the logic is correct.
- **Adjacent `u, v` (single edge):** `d = 1`, answer `2^0 = 1`.

---

## 🎯 Interview Takeaways
- The parity closed form `2^(d-1)` carries over from problem I; the new challenge is computing path length `d` for arbitrary node pairs quickly.
- `d = depth[u] + depth[v] - 2*depth[lca(u,v)]` is the canonical tree-distance formula.
- Binary lifting answers LCA in `O(log n)` after `O(n log n)` preprocessing — the standard tool for many path/ancestor queries.
- Lift the deeper node first to equalize depths, then lift both together until just below the LCA.

---

## 📌 Key Pattern
👉 **"Tree path length via LCA: d = depth[u] + depth[v] − 2·depth[lca], then apply the 2^(d-1) parity count per query."**

---

## 🔁 Related Problems
- 3558. Number of Ways to Assign Edge Weights I
- 1483. Kth Ancestor of a Tree Node
- 2646. Minimize the Total Price of the Trips
- 236. Lowest Common Ancestor of a Binary Tree

---

## 🚀 Final Thoughts
This Hard version keeps the same elegant parity insight from problem I but adds a multi-query twist that forces an efficient LCA. Binary lifting is the workhorse: precompute ancestors at power-of-two jumps, equalize depths, then climb in lockstep. With `d` in hand, each answer is a single fast-power call. The `u == v` guard is the small but essential detail that keeps `2^(d-1)` well defined.

---

✨ **Rule to remember:**
> "For many path queries on a tree, precompute binary-lifting LCA; the distance is depth[u]+depth[v]−2·depth[lca], and here the odd-weight count is 2^(distance−1)."
