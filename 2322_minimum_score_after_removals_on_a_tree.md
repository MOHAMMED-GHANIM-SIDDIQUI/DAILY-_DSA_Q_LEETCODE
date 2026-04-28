# 2322. Minimum Score After Removals on a Tree

## 🔗 Problem Link
https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Array, Tree, Depth-First Search, Bit Manipulation

---

## 🧩 Problem Summary
Given an undirected tree with `n` nodes, each having a value, remove exactly two edges to split the tree into three components. The score is the difference between the maximum and minimum XOR of the three components. Return the minimum possible score.

### 📌 Constraints
- `n == nums.length`
- `3 <= n <= 1000`
- `1 <= nums[i] <= 10^8`
- `edges.length == n - 1`
- `edges[i].length == 2`

---

## 💭 Intuition
👉 If we root the tree and precompute subtree XOR values and children sets, we can enumerate all pairs of edges to remove and efficiently compute the three component XOR values based on ancestor-descendant relationships.

---

## ⚡ Approach — DFS with Subtree XOR and Children Tracking

### 🧠 Idea
- Root the tree at node 0 and perform DFS to compute `subXors[u]` (XOR of all values in u's subtree) and `children[u]` (set of all descendant nodes).
- The total XOR of all nodes is `xors`.
- Enumerate all pairs of edges `(i, j)`. For each pair, determine the ancestor-descendant relationship of the two removed edges to compute the three component XOR values.
- Track the minimum difference between max and min of the three XOR values.

---

## 💻 Code

```cpp
class Solution {
 public:
  int minimumScore(vector<int>& nums, vector<vector<int>>& edges) {
    const int n = nums.size();
    const int xors = reduce(nums.begin(), nums.end(), 0, bit_xor());
    vector<int> subXors(nums);
    vector<vector<int>> tree(n);
    vector<unordered_set<int>> children(n);

    for (int i = 0; i < n; ++i)
      children[i].insert(i);

    for (const vector<int>& edge : edges) {
      const int u = edge[0];
      const int v = edge[1];
      tree[u].push_back(v);
      tree[v].push_back(u);
    }

    dfs(tree, 0, -1, subXors, children);

    int ans = INT_MAX;

    for (int i = 0; i < edges.size(); ++i) {
      int a = edges[i][0];
      int b = edges[i][1];
      if (children[a].contains(b))
        swap(a, b);
      for (int j = 0; j < i; ++j) {
        int c = edges[j][0];
        int d = edges[j][1];
        if (children[c].contains(d))
          swap(c, d);
        vector<int> cands;
        if (a != c && children[a].contains(c))
          cands = {subXors[c], subXors[a] ^ subXors[c], xors ^ subXors[a]};
        else if (a != c && children[c].contains(a))
          cands = {subXors[a], subXors[c] ^ subXors[a], xors ^ subXors[c]};
        else
          cands = {subXors[a], subXors[c], xors ^ subXors[a] ^ subXors[c]};
        ans = min(ans, ranges::max(cands) - ranges::min(cands));
      }
    }

    return ans;
  }

 private:
  pair<int, unordered_set<int>> dfs(const vector<vector<int>>& tree, int u,
                                    int prev, vector<int>& subXors,
                                    vector<unordered_set<int>>& children) {
    for (const int v : tree[u]) {
      if (v == prev)
        continue;
      const auto& [vXor, vChildren] = dfs(tree, v, u, subXors, children);
      subXors[u] ^= vXor;
      children[u].insert(vChildren.begin(), vChildren.end());
    }
    return {subXors[u], children[u]};
  }
};
```

---

## 🧠 Dry Run
### Input
```
nums = [5,5,2,4,4,2], edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]
```
### Steps
```
Total XOR = 5^5^2^4^4^2 = 0
Build tree rooted at 0, DFS to compute subXors and children.
subXors[0]=0, subXors[1]=0^5=depends on subtree...
Enumerate all (i,j) edge pairs, compute 3-component XOR values.
For each pair, compute max-min of {xor1, xor2, xor3}.
Return minimum score across all pairs.
```

---

## ⏱️ Time Complexity
```
O(n^2) — enumerate all pairs of edges, each check is O(1) with precomputed children sets.
```

## 💾 Space Complexity
```
O(n^2) — children sets can hold up to n elements each.
```

---

## ⚠️ Edge Cases
- Tree is a straight line (path graph).
- All node values are equal.
- Score of 0 is achievable when all three components have same XOR.

---

## 🎯 Interview Takeaways
- Subtree XOR can be computed bottom-up with DFS.
- Tracking children sets lets you determine ancestor-descendant relationships in O(1).
- XOR is its own inverse: removing a subtree's XOR from total gives the complement.

---

## 📌 Key Pattern
👉 **"Precompute subtree aggregates via DFS, then enumerate edge-removal pairs."**

---

## 🔁 Related Problems
- 2049. Count Nodes With the Highest Score
- 1110. Delete Nodes And Return Forest
- 2246. Longest Path With Different Adjacent Characters

---

## 🚀 Final Thoughts
This problem elegantly combines tree DFS, XOR properties, and enumeration. The key insight is that removing two edges creates three components whose XOR values can be derived from subtree XOR precomputation and ancestor-descendant relationships.

---

✨ **Rule to remember:**
> "Subtree XOR + children tracking lets you split a tree into components efficiently."
