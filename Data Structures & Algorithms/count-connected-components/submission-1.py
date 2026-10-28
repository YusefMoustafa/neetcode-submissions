from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # given an undirected graph of n nodes and list of edges where edges[i] = [ai, bi]
        # return the # of connected components in the graph

        # if we run dfs on a node and visit all its neighbors then that itself is one component. if we visit a nei and its not in a visited set, then we run dfs on it and add to the component. 

        # build our adj list where we map each node to its neighbors. its undirected

        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src) 
        
        # define our dfs function that will mark each node on its path
        visited = set()
        def dfs(node):
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        
        # iterate over range(n) and check if 
        components = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                components += 1
        return components

