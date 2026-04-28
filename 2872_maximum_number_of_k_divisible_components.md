# 2872. Maximum Number of K-Divisible Components

## 🔗 Problem Link
https://leetcode.com/problems/maximum-number-of-k-divisible-components/

## ⚡ Difficulty
Hard

## 🏷️ Topics
Tree, DFS, Graph

---

## 🧩 Problem Summary
Given a tree with `n` nodes, each having a value, find the maximum number of connected components you can obtain by removing edges such that the sum of values in each component is divisible by `k`.

### 📌 Constraints
- 1 <= n <= 3 * 10^4
- edges.length == n - 1
- 0 <= values[i] <= 10^9
- 1 <= k <= 10^9

---

## 💭 Intuition
👉 Use DFS to compute subtree sums. Whenever a subtree's sum is divisible by `k`, we can "cut" that subtree off — effectively incrementing the component count. The subtree contributes 0 to its parent since its sum is a multiple of `k`.

---

## ⚡ Approach — DFS with Greedy Cutting

### 🧠 Idea
- Build an adjacency list from the edges.
- Run DFS from root (node 0), computing the sum of each subtree.
- Whenever a subtree sum is divisible by `k`, increment the answer (this subtree forms its own component).
- Return the subtree sum to the parent for accumulation.

---

## 💻 Code

```cpp
class Solution {
 public:
  int maxKDivisibleComponents(int n, vector<vector<int>>& edges,
                              vector<int>& values, int k) {
    int ans = 0;
    vector<vector<int>> graph(n);

    for (const vector<int>& edge : edges) {
      const int u = edge[0];
      const int v = edge[1];
      graph[u].push_back(v);
      graph[v].push_back(u);
    }

    dfs(graph, 0, /*prev=*/-1, values, k, ans);
    return ans;
  }

 private:
  long dfs(const vector<vector<int>>& graph, int u, int prev,
           const vector<int>& values, int k, int& ans) {
    long treeSum = values[u];

    for (const int v : graph[u])
      if (v != prev)
        treeSum += dfs(graph, v, u, values, k, ans);

    if (treeSum % k == 0)
      ++ans;
    return treeSum;
  }
};
```

---

## 🧠 Dry Run
### Input
```
n = 5, edges = [[0,2],[1,2],[1,3],[2,4]], values = [1,8,1,4,4], k = 6
```
### Steps
```
Tree structure (rooted at 0):
       0(1)
       |
       2(1)
      / \
    1(8)  4(4)
    |
    3(4)

DFS:
  Node 3: sum=4, 4%6!=0 → return 4
  Node 1: sum=8+4=12, 12%6==0 → ans=1, return 12
  Node 4: sum=4, 4%6!=0 → return 4
  Node 2: sum=1+12+4=17, 17%6!=0 → return 17
  Node 0: sum=1+17=18, 18%6==0 → ans=2

Output: 2
```

---

## ⏱️ Time Complexity
```
O(n) — each node is visited exactly once in DFS
```

## 💾 Space Complexity
```
O(n) — adjacency list and recursion stack
```

---

## ⚠️ Edge Cases
- Single node tree: answer is 1 if the value is divisible by `k`.
- All values are 0: every possible cut is valid, so answer equals `n`.
- Total sum not divisible by `k`: impossible scenario (guaranteed valid input).

---

## 🎯 Interview Takeaways
- Greedy bottom-up DFS on trees: cut subtrees that satisfy a divisibility condition.
- Subtree sum problems are natural fits for post-order DFS.
- Using `long` to avoid integer overflow with large values.

---

## 📌 Key Pattern
👉 **"Greedy DFS Subtree Sum — cut when divisible"**

---

## 🔁 Related Problems
- 2440. Create Components With Same Value
- 834. Sum of Distances in Tree
- 337. House Robber III

---

## 🚀 Final Thoughts
The greedy insight is powerful: whenever a subtree sums to a multiple of `k`, cutting it off is always optimal because it doesn't affect the divisibility of the remaining tree's sum. This transforms a potentially complex partitioning problem into a simple DFS traversal.

---

✨ **Rule to remember:**
> In a tree partitioning problem, greedily cut subtrees whose sum is divisible by k — each valid cut is always beneficial.
