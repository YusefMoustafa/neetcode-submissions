class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        # given arr points where points[i] represents a point on the graph.
        # it costs |x1 - x2| + |y1 - y2| to connect 2 points on the graph.
        # we want to return the minimum cost it takes to connext all points together.
        # we can use prims algo since this will allow us to start at any arbitrary vertex and add the smallest neighboring edge weight until we've visited all vertices.

        # build an adj list where we map v1: (v2, wei) and vis versa. 
            # calculate the distance between 2 points |x1 - x2| + |y1 - y2|
        n = len(points)
        adj = defaultdict(list)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((j, dist))
                adj[j].append((i, dist))
        
        # start with an arbitrary point, say point[0]. preload the minHeap with its neighbors as [wei, node]. initialize visited set and store 0 in it.
        visited = set()
        visited.add(0)
        minHeap = []
        for nei, wei in adj[0]:
            heapq.heappush(minHeap, [wei, nei])
        
        total = 0

        # while our minHeap is nonempty (or we can say while len(visited) < n) we will pop off the min cost edge, make sure its not been visited, add it to visited, total += its weight, check its neighbors, make sure its not visited, add those non visited edges to the minHeap
        while minHeap:
            wei, point = heapq.heappop(minHeap)
            if point in visited:
                continue
            visited.add(point)
            total += wei
            for nei, neiW in adj[point]:
                if nei not in visited:
                    heapq.heappush(minHeap, [neiW, nei])

        # return total
        return total
