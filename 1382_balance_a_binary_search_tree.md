# 1382. Balance a Binary Search Tree

## 🔗 Problem Link
https://leetcode.com/problems/balance-a-binary-search-tree/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Binary Search Tree, Divide and Conquer, Greedy, Tree, Depth-First Search

---

## 🧩 Problem Summary
Given the root of a binary search tree, return a balanced BST with the same node values. A balanced BST is one where the depth of the two subtrees of every node never differs by more than 1.

### 📌 Constraints
- The number of nodes in the tree is in the range `[1, 10^4]`.
- `1 <= Node.val <= 10^5`

---

## 💭 Intuition
👉 An inorder traversal of a BST yields a sorted array. From a sorted array, we can build a balanced BST by always picking the middle element as the root — this is the classic "sorted array to BST" technique.

---

## ⚡ Approach — Inorder Traversal + Rebuild

### 🧠 Idea
- Perform an inorder traversal to collect all values in sorted order.
- Recursively build a balanced BST by selecting the middle element as root.
- The left half becomes the left subtree, the right half becomes the right subtree.

---

## 💻 Code

```python
class Solution:
  def balanceBST(self, root: TreeNode | None) -> TreeNode | None:
    nums = []

    def inorder(root: TreeNode | None) -> None:
      if not root:
        return
      inorder(root.left)
      nums.append(root.val)
      inorder(root.right)

    inorder(root)

    def build(l: int, r: int) -> TreeNode | None:
      if l > r:
        return None
      m = (l + r) // 2
      return TreeNode(nums[m],
                      build(l, m - 1),
                      build(m + 1, r))

    return build(0, len(nums) - 1)
```

---

## 🧠 Dry Run
### Input
```
root = [1, null, 2, null, 3, null, 4]  (a right-skewed BST)
```
### Steps
```
Inorder → nums = [1, 2, 3, 4]
build(0, 3): m=1 → root=2
  build(0, 0): m=0 → root=1 (leaf)
  build(2, 3): m=2 → root=3
    build(3, 3): m=3 → root=4 (leaf)
Result: balanced BST rooted at 2
```

---

## ⏱️ Time Complexity
```
O(n) — inorder traversal + rebuild each visit every node once
```

## 💾 Space Complexity
```
O(n) — for storing the sorted values array and recursion stack
```

---

## ⚠️ Edge Cases
- Single node → already balanced, return as is
- Already balanced BST → rebuild produces equivalent tree
- Fully skewed tree (linked list shape) → maximum rebalancing needed

---

## 🎯 Interview Takeaways
- "Inorder + rebuild" is the standard two-step approach for BST rebalancing.
- Picking the middle element guarantees minimal height.
- This technique is also used in converting sorted arrays/lists to BSTs.

---

## 📌 Key Pattern
👉 **"Flatten BST via inorder, then rebuild balanced BST from sorted array using divide and conquer."**

---

## 🔁 Related Problems
- 108. Convert Sorted Array to Binary Search Tree
- 109. Convert Sorted List to Binary Search Tree
- 1038. Binary Search Tree to Greater Sum Tree

---

## 🚀 Final Thoughts
A two-phase approach — flatten then rebuild — is simple and optimal. The sorted-array-to-BST construction is a fundamental technique every developer should know.

---

✨ **Rule to remember:**
> To balance a BST: inorder traversal → sorted array → pick middle as root recursively.
