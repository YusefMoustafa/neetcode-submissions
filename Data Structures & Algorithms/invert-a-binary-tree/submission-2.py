# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # to solve this iteratively we would use BFS which would require a queue to store the children of each node.
        # initialize the queue with root node
        # pop the leftmost node from q
        # swap that nodes left and right children
        # then add those children to the q if they exist
        # when the q is empty we can return the root of the inverted tree

        if not root:
            return None
        q = deque([root])


        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
        return root


