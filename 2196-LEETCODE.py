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
        
