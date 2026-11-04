from collections import defaultdict
import heapq
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        # given n cities labeled 0:n-1, and list edges where edges[i] holds [src_city, dst_city, weight]. edges are directed.
        # for every single city, we want to count the other cities that can be reached via a route that is <= distanceThreshold.
        # return the label of a city that has the smallest # of cities it can reach. if cities tie, return the greatest label. 

        # build adj list where src_city maps to (dst_city, weight). this will allow us to later traverse a cities neighbors for a route that we can take.

        adj = defaultdict(list)
        for s, d, wei in edges:
            adj[s].append((d, wei))
            adj[d].append((s, wei)) 
        # minHeap = []
        # adj = { [0:(1,2)], [1:(0,2),(2:2)], [2:(1,2),(3,2)], [3:(2,2)] }
        # visited = {0,1}

        # djikstra allows us to find the smallest route from src_city to dst_city, and we can tweak it to be bounded by the distanceThreshold.
        # we will run djikstra from each city and record the total # of cities that it can take in its path by adding the cities to a visited set and then returning the length of the set (minus the src city).
        # initialize a minHeap with the src_city/weight.
        # while the heap is nonempty, we will pop off the heap and check if we alr visited this city, if so continue. otherwise add it to visited. 
        # then we will iterate over this cities neighbors and their respective weights. check if neiWeight+weight <= distanceThreshold and neiCity not in visited, if so add that weight/city to the heap.
        # then return len(visited) - 1.

        def djikstra(city):
            minHeap = [(0, city)]
            visited = set()
            while minHeap:
                wei, city = heapq.heappop(minHeap)
                if city in visited:
                    continue
                visited.add(city)
                for nei, neiWei in adj[city]:
                    if neiWei+wei <= distanceThreshold and nei not in visited:
                        heapq.heappush(minHeap, (neiWei+wei, nei))
            return len(visited) - 1
        # run djikstra n-1 times and hold its return value in count var.
        # if that count <= smallest_count, then set smallest_count = count
        # then set that respective city = res_city.
        # return res_city. 
        smallest_cnt = float('inf')
        res_city = -1
        for city in range(n):
            cnt = djikstra(city)
            if cnt <= smallest_cnt:
                smallest_cnt = cnt
                res_city = city
        return res_city

            
