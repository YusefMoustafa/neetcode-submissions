# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # using dfs instead

        # since we want to visit each node level by level, with dfs instead of using a queue we would use recursion and pass the curr depth of the tree.
        # for each node we check if this is a node of a new level (do this by checking if len(res) == depth that we will pass into the function) and if true we append a empty list to res so that way we can process all nodes into that list on that level, then we will append the node value, and recursively check the left and right subtrees with a +1 depth (since its next level). this will allow all the nodes to be processed top->bottom left to right level by level. then return res list. 

        res = []

        def dfs(root, depth):
            if not root:
                return None
            
            if len(res) == depth:
                res.append([])
            
            res[depth].append(root.val)

            dfs(root.left, depth+1)
            dfs(root.right, depth+1)

        dfs(root, 0)
        return res