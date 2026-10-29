from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # given n nodes, and a list of undirected edges
        # return True or false if its a valid tree
        # valid tree = acyclic and fully connected

        # build adj list that maps each node to its neighbors (undirected)

        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        # use dfs to each all of a nodes neighbors and record them in a visited set.
        # if node were on is alr in visited, then theres a cycle, so return False
        visited = set()
        def dfs(node, par):
            if node in visited:
                return False
            visited.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True
                
        # iterate over range(nodes), if dfs(node) and n == len(visited), return True. return false

        if dfs(0, -1) and n == len(visited):
            return True
        return False