class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # we want to find the edge that causes the cycle in the graph and return that edge.
        # if we use union find on the edges, we can find the root of 2 nodes and if their roots are equal then we know that edge between those 2 nodes are causing the cycle. 
        # initialize parents dictionary that maps each node : its parent (itself) at first because we are assuming each node is its own graph
        # initialize rank dictionary that will map a node : its height. Since each node is its own parent we set them all to be rank 0.
        parent = {}
        rank = {}
        nodes = len(edges)
        for i in range(1, nodes+1):
            parent[i] = i
            rank[i] = 0
        # define a find function that finds the root of a node
            # if the node == its parent, then that is the root. return parent
            # otherwise, we will recursively do path compression where we    have parent[node] = find(parent[node]) until the node is its own parent.

        def find(node):
            if node == parent[node]:
                return parent[node]
            parent[node] = find(parent[node])
            return parent[node]
        # define a union function that will attempt to union each edge from edges. We will call find on our 2 nodes. 
            # if they are equal there is a cycle, so we reutrn the edge
            # if the rank of node1 > node2, then set node1 as parent of node2
            # if the rank of node1<node2, set node2 as parent of node1
            # if theyre equal then we arbitrarily choose one to be parent
                # increment its rank by 1

        def union(node1, node2):
            root1, root2 = find(node1), find(node2)
            if root1 == root2:
                return False
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
            return True
        
        # now we just iterate over edges and if not union[ai, bi], return [ai, bi]

        for ai, bi in edges:
            if not union(ai, bi):
                return [ai, bi]





