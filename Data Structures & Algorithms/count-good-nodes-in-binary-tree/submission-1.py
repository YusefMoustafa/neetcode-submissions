# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        def dfs(root, maxNode):

            total = 0

            if not root:
                return 0

            if root.val == maxNode:
                total += 1
            elif root.val > maxNode:
                total += 1
                maxNode = root.val

            total += dfs(root.left, maxNode)
            total += dfs(root.right, maxNode)

            return total
        
        return dfs(root, root.val)