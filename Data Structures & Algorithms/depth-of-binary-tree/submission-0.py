# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # recursively check left and right subtrees.
        # establish a base case if not node return 0
        # return 1 + max(left subtree, right subtree)
        # this will allow us to return the max depth always since we take the subtree with the larger amount and then we add 1 to it to account for the node we are curr on.

        if not root:
            return 0
        
        left_tree = self.maxDepth(root.left)
        right_tree = self.maxDepth(root.right)
        return max(left_tree, right_tree) + 1
