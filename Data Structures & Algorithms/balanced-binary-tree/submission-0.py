# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left = self.height(root.left)
        right = self.height(root.right)
        if abs(left - right) > 1:
            return False
        left_tree = self.isBalanced(root.left)
        right_tree = self.isBalanced(root.right)
        return left_tree and right_tree
        

    def height(self, node):
        if not node:
            return 0
        left = self.height(node.left)
        right = self.height(node.right)
        return 1 + max(left, right)

