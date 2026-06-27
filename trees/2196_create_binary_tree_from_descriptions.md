# 2196. Create Binary Tree From Descriptions

## 🔗 Problem Link
https://leetcode.com/problems/create-binary-tree-from-descriptions/

## ⚡ Difficulty
Medium

## 🏷️ Topics
Array, Hash Table, Tree, Binary Tree

---

## 🧩 Problem Summary

You are given a 2D array `descriptions` where `descriptions[i] = [parent, child, isLeft]`. Each entry means `child` is a node attached under `parent`, as the **left** child if `isLeft == 1` and the **right** child if `isLeft == 0`. All values are unique and the descriptions are guaranteed to form a valid binary tree. Build the tree and return its **root**.

### 📌 Constraints
- `1 <= descriptions.length <= 10^4`
- `descriptions[i].length == 3`
- `1 <= parent_i, child_i <= 10^5`
- `0 <= isLeft_i <= 1`
- The descriptions form a valid binary tree.

---

## 💭 Intuition

👉 Every node mentioned as a `child` has a parent, so the **root is the unique value that never appears in the child column**. If we first materialize a `TreeNode` for every value we see and remember which values are children, the root falls out by elimination. Once all nodes exist, a second pass simply wires up the left/right pointers.

---

## ⚡ Approach — Hash Map + Children Set

### 🧠 Idea
- **Pass 1:** Iterate over every description. Lazily create a `TreeNode` in a dict `nodes` for both `parent` and `child` (so each value maps to exactly one node object). Record every `child` value in a `children` set.
- **Find root:** Scan the parents; the first parent that is *not* in `children` is the root (it is the only such value).
- **Pass 2:** For each description, link `nodes[parent].left = nodes[child]` if `is_left` is truthy, otherwise `nodes[parent].right = nodes[child]`.
- Return the root node.

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
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        # Pass 1: create nodes and collect children
        for parent, child, _ in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)

            children.add(child)

        # Find root
        root = None
        for parent, _, _ in descriptions:
            if parent not in children:
                root = nodes[parent]
                break

        # Pass 2: build tree
        for parent, child, is_left in descriptions:
            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

        return root
```

---

## 🧠 Dry Run

### Input
```
descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
```

### Steps
```
Pass 1 (create nodes, collect children):
  [20,15,1] -> nodes={20,15}            children={15}
  [20,17,0] -> nodes={20,15,17}         children={15,17}
  [50,20,1] -> nodes={20,15,17,50}      children={15,17,20}
  [50,80,0] -> nodes={...,80}           children={15,17,20,80}
  [80,19,1] -> nodes={...,19}           children={15,17,20,80,19}

Find root (scan parents 20,20,50,50,80):
  20 in children? yes -> skip
  20 in children? yes -> skip
  50 in children? no  -> root = nodes[50]   (break)

Pass 2 (link pointers):
  [20,15,1] is_left -> 20.left  = 15
  [20,17,0]         -> 20.right = 17
  [50,20,1] is_left -> 50.left  = 20
  [50,80,0]         -> 50.right = 80
  [80,19,1] is_left -> 80.left  = 19

Resulting tree (root 50):
          50
        /    \
      20      80
     /  \    /
    15  17  19

return nodes[50]
```

---

## ⏱️ Time Complexity
```
O(n)
```
Each of the `n` descriptions is touched a constant number of times across the three passes; dict and set operations are O(1) average.

---

## 💾 Space Complexity
```
O(n)
```
The `nodes` dict holds one `TreeNode` per distinct value (up to `n + 1`) and the `children` set holds up to `n` values.

---

## ⚠️ Edge Cases
- **Single edge** (`descriptions = [[p, c, isLeft]]`): one node is a child, the other is the root — handled by elimination.
- **Same value as left/right in different rows:** values are unique, so the dict guarantees one node object reused everywhere.
- **Root referenced after children rows:** scanning all parents (not just the first) ensures we still find the non-child parent.

---

## 🎯 Interview Takeaways
- The "node with no parent" trick = the root is the value never seen as a child; a set difference identifies it cleanly.
- Materializing nodes first, then wiring pointers, avoids order-dependence in the input.
- Using a dict keyed by value to dedupe `TreeNode` creation is the core idea for "build graph/tree from edge list" problems.

---

## 📌 Key Pattern
👉 **"Build a tree from an edge list: map values → nodes, find the root as the only non-child, then link pointers."**

---

## 🔁 Related Problems
- 1485. Clone Binary Tree With Random Pointer
- 1361. Validate Binary Tree Nodes
- 889. Construct Binary Tree from Preorder and Postorder Traversal
- 297. Serialize and Deserialize Binary Tree

---

## 🚀 Final Thoughts
This is a clean "construct from descriptions" problem where the trick is recognizing the root as the unique value that is never a child. By separating node creation from pointer linking, the algorithm stays O(n) and order-independent. The `children` set is the workhorse that turns root-finding into a simple membership test.

---

✨ **Rule to remember:**
> "In an edge/description list, the root is the only node that never appears as a child — track children in a set and the root reveals itself."
