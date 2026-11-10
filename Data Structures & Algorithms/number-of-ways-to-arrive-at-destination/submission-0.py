class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        # given n intersections labeled 0 to n-1 and list of roads where roads[i] = [src, dst, time] where it takes time to get from src to dst. 
        # we want to return the # of different routes whose routes take the shortest possible travel time from intersection 0 to n-1. 
        # return the count module 10^6 +7

        # build an adj list for the undirected edges. 
        adj = defaultdict(list)
        for src,dst,wei in roads:
            adj[src].append((dst,wei))
            adj[dst].append((src,wei))
        
        # we will use djisktra to find the shortest path from 0 to n-1 since all routes are positive and and we want the cheapest route. 
            # we will keep a dist[node] list, where each node contains its shortest path. a minHeap will allow us to take the intersection with the smallest wei next.
        # we want the # of routes that completed in shortest time. 
            # we can create a ways[node] arr where each node is an intersection and we keep track of the # of ways it took to complete shortest time from 0 to that node
        # 
        MOD = 10**9 + 7
        minHeap = [(0,0)] # initialize with (wei, dst) for intersection 0.
        min_cost = [float('inf')] * n
        min_cost[0] = 0
        path_count = [0] * n
        path_count[0] = 1
        while minHeap:
            cost, node = heapq.heappop(minHeap)
            for nei, nei_cost in adj[node]:
                if cost + nei_cost < min_cost[nei]:
                    min_cost[nei] = cost + nei_cost
                    path_count[nei] = path_count[node]
                    heapq.heappush(minHeap, (cost+nei_cost, nei))
                elif cost + nei_cost == min_cost[nei]:
                    path_count[nei] += path_count[node]
                    path_count[nei] = path_count[nei] % MOD
        return path_count[-1]


