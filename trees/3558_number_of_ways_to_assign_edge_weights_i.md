# 3558. Number of Ways to Assign Edge Weights I

## 🔗 Problem Link
https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Tree, Depth-First Search, Math

---

## 🧩 Problem Summary

You are given a tree rooted at node `1` with `n` nodes and `n - 1` edges. Each edge is assigned a weight of either `1` or `2`. Let `x` be a **deepest** node (the path from root `1` to `x` has the maximum number of edges). Count the number of weight assignments along that root-to-deepest path whose **total weight is odd**, modulo `10^9 + 7`.

### 📌 Constraints
- `2 <= n <= 10^5`
- `edges.length == n - 1`
- `edges[i] = [u_i, v_i]` describe a valid tree rooted at node `1`.
- Each edge weight is independently chosen from `{1, 2}`.

---

## 💭 Intuition

👉 Only the **length of the path** (number of edges `d` from root to the deepest node) matters. Each of the `d` edges is `1` or `2`, giving `2^d` total assignments. The parity of the sum is decided purely by **how many edges are weight `1`** (weight `2` never changes parity). Among `2^d` assignments, exactly **half** produce an odd sum — so the answer is `2^(d-1) mod (10^9+7)`. We just need `d = max depth in edges`, found with a single DFS.

---

## ⚡ Approach — DFS for Max Depth + Power of Two

### 🧠 Idea
- Build an adjacency list `g` from the edges (undirected, since the tree is given as edges).
- Run a DFS from root `1` with parent `0`; `dfs` returns the **maximum depth in edges** of the subtree rooted at the current node. For each non-parent child `y`, recurse and take `max(max_dep, dfs(y) + 1)`.
- Let `d = max_dep` be the overall maximum depth. The number of odd-sum assignments over `d` edges is `2^(d-1)`.
- Return `pow(2, d - 1, MOD)` using fast modular exponentiation.

---

## 💻 Code

```python
class Solution:
    MOD = 10**9 + 7

    def dfs(self, g: list, x: int, f: int) -> int:
        max_dep = 0
        for y in g[x]:
            if y == f:
                continue
            max_dep = max(max_dep, self.dfs(g, y, x) + 1)
        return max_dep

    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        max_dep = self.dfs(g, 1, 0)
        return pow(2, max_dep - 1, self.MOD)
```

---

## 🧠 Dry Run

### Input
```
edges = [[1,2],[1,3],[3,4],[3,5]]
n = 5
```

### Steps
```
Adjacency list g:
  1: [2, 3]
  2: [1]
  3: [1, 4, 5]
  4: [3]
  5: [3]

DFS from (x=1, f=0):
  child 2: dfs(2,1) -> only neighbor 1 == parent -> returns 0
           max_dep = max(0, 0+1) = 1
  child 3: dfs(3,1):
             child 4: dfs(4,3) -> returns 0 -> max_dep = max(0,1) = 1
             child 5: dfs(5,3) -> returns 0 -> max_dep = max(1,1) = 1
             returns 1
           max_dep = max(1, 1+1) = 2
  returns 2

d = max_dep = 2   (deepest path e.g. 1 -> 3 -> 4, two edges)

answer = pow(2, 2-1, MOD) = 2^1 = 2
```

Check: two edges, each in {1,2}. Sums: (1,1)=2 even, (1,2)=3 odd, (2,1)=3 odd, (2,2)=4 even → 2 odd-sum assignments. ✓

---

## ⏱️ Time Complexity
```
O(n)
```
The DFS visits each of the `n` nodes once and traverses each edge a constant number of times. Building the adjacency list is also O(n), and `pow` is O(log d).

---

## 💾 Space Complexity
```
O(n)
```
The adjacency list stores `2(n-1)` entries, and the recursive DFS stack can reach depth O(n) in a degenerate (path-like) tree.

---

## ⚠️ Edge Cases
- **`d = 1` (root has a deepest child one edge away):** `2^(1-1) = 2^0 = 1`, the single odd assignment being weight `1`.
- **Path-like (skewed) tree:** DFS recursion can be as deep as `n`; correctness is unaffected.
- **Multiple deepest nodes:** only the depth `d` matters, so any deepest node gives the same count.

---

## 🎯 Interview Takeaways
- Weight `2` is "parity-neutral", so the sum's parity is governed solely by the count of weight-`1` edges → exactly half of all assignments are odd.
- Reducing a counting problem to a single parameter (`d`) plus a closed-form `2^(d-1)` is the key insight.
- A standard parent-tracking DFS computes max depth in O(n) without needing visited markers (it's a tree).

---

## 📌 Key Pattern
👉 **"Half of all ±-parity assignments over d independent binary choices are odd → 2^(d-1)."**

---

## 🔁 Related Problems
- 3559. Number of Ways to Assign Edge Weights II
- 543. Diameter of Binary Tree
- 1448. Count Good Nodes in Binary Tree
- 104. Maximum Depth of Binary Tree

---

## 🚀 Final Thoughts
The problem looks like it needs heavy combinatorics, but the parity argument collapses it to "compute the deepest path length, return `2^(d-1)`." The only real work is a DFS for max depth. Recognizing that weight-2 edges don't affect parity is what unlocks the clean closed form.

---

✨ **Rule to remember:**
> "Over d independent {odd, even} weight choices, exactly half of the 2^d assignments are odd — the answer is 2^(d-1)."
