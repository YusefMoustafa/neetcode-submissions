# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# given root of binary tree, return true if its a valid BST, else false
# all values left of the node must be strictly < and all values to the right of the node must be strictly >
# every subtree must also be a BST.
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(root, left, right): # helper function to validate each node in tree recursively
            if not root:
                return True

            if not (left < root.val < right):
                return False
            
            return valid(root.left, left, root.val) and valid(root.right, root.val, right)


        return valid(root, float('-inf'), float('inf'))