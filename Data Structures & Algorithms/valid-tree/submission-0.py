from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) > n-1:
            return False

        adj = defaultdict(list)

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        seen = set()

        def dfs(node, parent):
            if node in seen:
                return False
            
            seen.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0,-1) and n == len(seen)

                    