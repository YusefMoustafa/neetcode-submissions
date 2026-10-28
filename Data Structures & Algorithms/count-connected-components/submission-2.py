class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # given undirected graph of n nodes and an arr edges. 
        # return # of connected components in the graph

        # use union-find to union components and decrement the # of components and whatever components left are the total # of connected components
        # initialize each node as its own component. its parent will be itself
        # initialize the height of each component to be 0

        components = {}
        heights = {}
        for i in range(n):
            components[i] = i
            heights[i] = 0
        # def the find function that will return the root of a node
            # if that node == to its parent, return its parent
            # otherwise recrusively call find on its parent and set it equal to parent[node]. this will have our node point to the root. 
            # return parent[node]

        def find(node):
            if node == components[node]:
                return node
            components[node] = find(components[node])
            return components[node]
        # def the union fuction that will union 2 nodes that we will get from the edges arr. if we are able to union them then we will decrement components by 1. 
            # initialize root1 and root2 to find(node1) and find(node2)
            # if the 2 roots are the same, meaning they are in the same component that means theres a cycle, so return False
            # now we union by height (rank). we set the greater height node as the parent and the other as its child and vis versa. 
            # if theyre equal then we arbitrarily choose one as the parent
            # then we return True

        def union(node1, node2):
            root1, root2 = find(node1), find(node2)
            if root1 == root2:
                return False
            if root1 > root2:
                components[root2] = root1
            elif root1 < root2:
                components[root1] = root2
            else:
                components[root2] = root1
                heights[root1] += 1
            return True
        # now we iterate over edges, and for each pair if union(a,b) comes back true then we decrement components
        res = n
        for ai, bi in edges:
            if union(ai,bi):
                res -= 1
        
        # return components
        return res