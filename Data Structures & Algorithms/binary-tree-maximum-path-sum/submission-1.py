# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = root.val

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # make sure we dont consider any negative val nodes
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # update our res that sums node.val, leftMax and rightMax
            res = max(res, (root.val + leftMax + rightMax))
            
            # return the best path to the parent node (either left or right node + node.val)
            return root.val + max(leftMax, rightMax)

        # invoke the function
        dfs(root)
        return res