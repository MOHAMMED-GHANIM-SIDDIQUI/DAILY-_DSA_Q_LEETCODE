# 110. Balanced Binary Tree

## 🔗 Problem Link
https://leetcode.com/problems/balanced-binary-tree/

## ⚡ Difficulty
Easy

## 🏷️ Topics
Tree, Depth-First Search, Binary Tree, Recursion

---

## 🧩 Problem Summary

Given a binary tree, determine if it is height-balanced. A height-balanced binary tree is one in which the depth of the two subtrees of every node never differs by more than one.

### 📌 Constraints
- The number of nodes in the tree is in the range `[0, 5000]`
- `-10^4 <= Node.val <= 10^4`

---

## 💭 Intuition

👉 A tree is balanced if and only if: (1) the height difference between left and right subtrees at the root is at most 1, AND (2) both the left and right subtrees are themselves balanced. This naturally leads to a recursive top-down approach where we compute depth at each node and check balance recursively.

---

## ⚡ Approach — Top-Down Recursion

### 🧠 Idea

- Define a helper `maxDepth(root)` that returns the height of a subtree.
- At each node, check that `|maxDepth(left) - maxDepth(right)| <= 1`.
- Recursively verify that both left and right subtrees are also balanced.
- Return `True` only if all three conditions hold.

---

## 💻 Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isBalanced(self, root: TreeNode | None) -> bool:
    if not root:
      return True

    def maxDepth(root: TreeNode | None) -> int:
      if not root:
        return 0
      return 1 + max(maxDepth(root.left), maxDepth(root.right))

    return (abs(maxDepth(root.left) - maxDepth(root.right)) <= 1 and
            self.isBalanced(root.left) and
            self.isBalanced(root.right))
```

---

## 🧠 Dry Run

### Input
```
    3
   / \
  9  20
     / \
    15   7
```

### Steps
```
isBalanced(3):
  maxDepth(9) = 1
  maxDepth(20) = 2
  |1 - 2| = 1 <= 1 ✓
  isBalanced(9):
    maxDepth(None) = 0, maxDepth(None) = 0
    |0 - 0| = 0 <= 1 ✓
    isBalanced(None) = True, isBalanced(None) = True
    → True
  isBalanced(20):
    maxDepth(15) = 1, maxDepth(7) = 1
    |1 - 1| = 0 <= 1 ✓
    isBalanced(15) = True, isBalanced(7) = True
    → True
  → True
```

---

## ⏱️ Time Complexity

```
O(n log n)
```

In a balanced tree, `maxDepth` is called at each level, and each call traverses its subtree. In the worst case (skewed tree), this degrades to O(n²).

---

## 💾 Space Complexity

```
O(n)
```

Due to the recursion stack, which can be O(n) deep for a skewed tree.

---

## ⚠️ Edge Cases

- **Empty tree:** `root = None` → `True` (an empty tree is balanced)
- **Single node:** `root = TreeNode(1)` → `True`
- **Skewed tree:** `1 → 2 → 3 → 4` → `False`

---

## 🎯 Interview Takeaways

- This top-down approach is intuitive but recomputes depths multiple times. A bottom-up approach returning -1 for imbalance is O(n).
- Understanding the definition of "height-balanced" is critical — every node must satisfy the condition, not just the root.
- Tree problems almost always use recursion; practice thinking in terms of subtree properties.
- Know both top-down and bottom-up approaches for follow-up questions.

---

## 📌 Key Pattern

👉 **"Check a property at every node recursively: validate root, then recurse on children."**

---

## 🔁 Related Problems

- 104. Maximum Depth of Binary Tree
- 111. Minimum Depth of Binary Tree
- 543. Diameter of Binary Tree
- 236. Lowest Common Ancestor of a Binary Tree

---

## 🚀 Final Thoughts

Balanced Binary Tree is a foundational tree problem. The top-down recursive approach here is clean and easy to understand, though a bottom-up O(n) approach exists for optimization.

---

✨ **Rule to remember:**
> "A tree is balanced only if every subtree is balanced — check locally, verify globally."
