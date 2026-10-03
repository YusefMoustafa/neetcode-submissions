# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # [withRoot, withoutRoot]
        def dfs(root):
            if not root:
                return [0,0]

            leftPair = dfs(root.left)
            rightPair = dfs(root.right)

            withNode = root.val + leftPair[1] + rightPair[1]
            withoutNode = max(leftPair) + max(rightPair)

            return [withNode, withoutNode]
        
        return max(dfs(root))