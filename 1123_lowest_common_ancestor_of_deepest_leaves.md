# 1123. Lowest Common Ancestor of Deepest Leaves

## 🔗 Problem Link
https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Tree, Depth-First Search, Binary Tree

---

## 🧩 Problem Summary

Given the root of a binary tree, return the lowest common ancestor (LCA) of its deepest leaves. The deepest leaves are all leaves at the maximum depth. Their LCA is the deepest node that has all of them as descendants.

### 📌 Constraints
- The number of nodes is in the range `[1, 1000]`.
- `0 <= Node.val <= 1000`
- The values of the nodes are unique.

---

## 💭 Intuition

👉 At each node, compare the depths of the left and right subtrees. If they are equal, the current node is the LCA of the deepest leaves in its subtree. If one side is deeper, the LCA lies on that side.

---

## ⚡ Approach — DFS Returning (LCA, depth)

### 🧠 Idea
- Define a struct `T` holding a `TreeNode*` (the LCA) and an `int` (the depth).
- DFS returns the LCA and max depth for each subtree.
- If left depth > right depth, propagate the left result.
- If right depth > left depth, propagate the right result.
- If equal, the current node is the LCA at depth + 1.

---

## 💻 Code

```cpp
struct T {
  TreeNode* lca;
  int depth;
};

class Solution {
 public:
  TreeNode* lcaDeepestLeaves(TreeNode* root) {
    return dfs(root).lca;
  }

 private:
  T dfs(TreeNode* root) {
    if (root == nullptr)
      return {nullptr, 0};
    const T left = dfs(root->left);
    const T right = dfs(root->right);
    if (left.depth > right.depth)
      return {left.lca, left.depth + 1};
    if (left.depth < right.depth)
      return {right.lca, right.depth + 1};
    return {root, left.depth + 1};
  }
};
```

---

## 🧠 Dry Run

### Input
```
Tree:     3
         / \
        5   1
       / \
      6   2
```

### Steps
```
dfs(6) → {6, 1}
dfs(2) → {2, 1}
dfs(5): left.depth(1) == right.depth(1) → {5, 2}
dfs(1): left=null(0), right=null(0) → {1, 1}
dfs(3): left.depth(2) > right.depth(1) → {5, 3}

Output: node 5 (deepest leaves are 6 and 2, their LCA is 5)
```

---

## ⏱️ Time Complexity
```
O(n)
```
Each node is visited exactly once.

---

## 💾 Space Complexity
```
O(h)
```
Where `h` is the height of the tree (recursion stack).

---

## ⚠️ Edge Cases
- Single node → that node is both the deepest leaf and the LCA.
- Perfect binary tree → the root is the LCA of all deepest leaves.
- Skewed tree → the deepest leaf itself is the LCA.

---

## 🎯 Interview Takeaways
- Returning multiple values (LCA + depth) from DFS is a powerful pattern.
- Comparing subtree depths at each node elegantly identifies the LCA.
- This problem is equivalent to LeetCode 865 (Smallest Subtree with all the Deepest Nodes).
- Using a struct for the return type keeps the code readable.

---

## 📌 Key Pattern
👉 **"Post-order DFS returning (node, depth) — when both subtrees have equal max depth, the current node is the LCA."**

---

## 🔁 Related Problems
- 865 - Smallest Subtree with all the Deepest Nodes (identical problem)
- 236 - Lowest Common Ancestor of a Binary Tree
- 104 - Maximum Depth of Binary Tree

---

## 🚀 Final Thoughts
An elegant recursive solution where the LCA "bubbles up" naturally. The equal-depth check at each node is the key insight that makes this concise and efficient.

---

✨ **Rule to remember:**
> "When left and right subtree depths match, the current node is the LCA of the deepest leaves."
