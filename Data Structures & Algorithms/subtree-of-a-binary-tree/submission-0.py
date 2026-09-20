# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
        
        if self.isEqual(root,subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        # given a root and subroot binary trees. 
        # return True if subroot is a subtree of root

        # recursively: we will go through root recursively using DFS and for each node we will check to see if its subtree is equal to subroot by using a helper function that returns true if the 2 subtrees are equal. 

    def isEqual(self, root, subRoot):

        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False
        
        return self.isEqual(root.left, subRoot.left) and self.isEqual(root.right, subRoot.right)