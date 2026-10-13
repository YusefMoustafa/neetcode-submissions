from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        adjList = defaultdict(list)
        seen = set()

        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        
        # when you run dfs on a node, it marks  every single node that has a path from it, which makes up the entire component. so we do this by checking if all the nodes neighbors have already been seen
        def dfs(node):
            for nei in adjList[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)
             

        components = 0
        for node in range(n):
            if node not in seen:
                seen.add(node)
                dfs(node)
                components += 1
        return components