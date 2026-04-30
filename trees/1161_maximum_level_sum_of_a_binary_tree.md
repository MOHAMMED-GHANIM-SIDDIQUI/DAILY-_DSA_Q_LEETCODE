# 1161. Maximum Level Sum of a Binary Tree

## 🔗 Problem Link
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Tree, Depth-First Search, Breadth-First Search, Binary Tree

---

## 🧩 Problem Summary

Given the root of a binary tree, return the smallest level number (1-indexed) such that the sum of all node values at that level is maximized.

### 📌 Constraints
- The number of nodes is in the range `[1, 10^4]`.
- `-10^5 <= Node.val <= 10^5`

---

## 💭 Intuition

👉 Compute the sum of each level, then return the 1-indexed level with the maximum sum (smallest level if there's a tie).

👉 DFS can accumulate level sums into an array just as effectively as BFS.

---

## ⚡ Approach — DFS with Level Sums Array

### 🧠 Idea
- Maintain a list `levelSums` where `levelSums[i]` stores the sum of level `i+1`.
- DFS through the tree, expanding the list when a new level is reached.
- After traversal, find the index of the maximum sum and return it + 1 (1-indexed).

---

## 💻 Code

```python
class Solution:
  def maxLevelSum(self, root: TreeNode | None) -> int:
    # levelSums[i] := the sum of level (i + 1) (1-indexed)
    levelSums = []

    def dfs(root: TreeNode | None, level: int) -> None:
      if not root:
        return
      if len(levelSums) == level:
        levelSums.append(0)
      levelSums[level] += root.val
      dfs(root.left, level + 1)
      dfs(root.right, level + 1)

    dfs(root, 0)
    return 1 + levelSums.index(max(levelSums)
```

---

## 🧠 Dry Run

### Input
```
Tree:     1
         / \
        7   0
       / \
      7  -8
```

### Steps
```
dfs(1, 0): levelSums = [1]
dfs(7, 1): levelSums = [1, 7]
dfs(7, 2): levelSums = [1, 7, 7]
dfs(-8, 2): levelSums = [1, 7, -1]
dfs(0, 1): levelSums = [1, 7, -1]

levelSums = [1, 7, -1]
max = 7 at index 1 → return 1 + 1 = 2
Output: 2
```

---

## ⏱️ Time Complexity
```
O(n)
```
Each node is visited exactly once during DFS.

---

## 💾 Space Complexity
```
O(h)
```
Where `h` is the height of the tree — for the recursion stack and the levelSums array.

---

## ⚠️ Edge Cases
- Single node → return level 1.
- All negative values → the least negative level wins.
- Multiple levels with the same max sum → return the smallest level number.

---

## 🎯 Interview Takeaways
- DFS with a level parameter can compute level-wise aggregates without BFS.
- Using `list.index(max(list))` naturally returns the first (smallest) index on ties.
- BFS is an equally valid alternative for this problem.
- 1-indexed vs 0-indexed conversion is a common source of off-by-one bugs.

---

## 📌 Key Pattern
👉 **"DFS with level tracking — accumulate per-level statistics in an array indexed by depth."**

---

## 🔁 Related Problems
- 102 - Binary Tree Level Order Traversal
- 515 - Find Largest Value in Each Tree Row
- 637 - Average of Levels in Binary Tree

---

## 🚀 Final Thoughts
A clean DFS approach that avoids the overhead of a queue-based BFS. The level sums array grows dynamically as new depths are encountered, making the solution both simple and efficient.

---

✨ **Rule to remember:**
> "DFS with a depth parameter can do anything BFS can — just store results by level."
