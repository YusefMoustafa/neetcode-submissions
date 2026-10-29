class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # given n nodes and a list of undirected edges
        # determine whether these edges make up a valid tree (connected, acyclic)
        # use union find to determine if theres any cycles

        # initialize n graphs, where each graph is a node pointing at its parent
        # initialize the rank/height of each graph to be 0 since they are their own parent. 
        
        parent, rank = {}, {}
        for i in range(n):
            parent[i] = i
            rank[i] = 0

        # def find function to return the root of a node. if that node is equal to its parent, then thats the root. otherwise we set parent[node] = find(parent[node]). this path compression allows us to find roots in o(1) time.

        def find(node):
            if node == parent[node]:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        # def union function to attempt and union 2 root nodes if they are not equal. if theyre equal then theres a cycle. return false. otherwise we can union the roots by rank and if their rank is equal choose one root as parent and increment its rank.
        components = n
        def union(node1, node2):
            nonlocal components
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
            components -= 1
            return True
        # we can keep track of how many graphs there are and if it equal to 1 and we return True then we can return True.

        for ai, bi in edges:
            if not union(ai, bi):
                return False
        return components == 1


