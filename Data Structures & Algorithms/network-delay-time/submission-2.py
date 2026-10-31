from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # given graph with n directed nodes (1-n) and a list of directed edges named times where times[i] = (ui,vi,ti)
        # ui is the src node, vi is the target node, ti is the time it takes for a signal to travel from the source to the target node. (>=0)
        # given int k, which is the node that will start with the signal.
        # return min time for all nodes to recieve the signal.
        # if all nodes cannot recieve the signal, return -1.

        # from the times array, we can build an adj list where we map each source node to its (destination, time) using a hashmap.
        
        adj = defaultdict(list)
        for src, dst, time in times:
            adj[src].append((dst, time))
        # we can use dijkstra in order to find the shortest path to all other nodes from a source node.
        # initialize the shortest path hashmap that will map the node to its shortest path from the src node. 
        # initialize a minHeap with the src node and its weight which will be 0
        # while the minHeap is not empty, we will unpack the top node and weight
        # then we check if that node already has a shortest val, if so continue
        # if not then we will map that node to the weight since that will inevitably be the shortest possible path since that is the smallest val in the minHeap and there are no neg value times.

        shortest = {}
        minHeap = [(0, k)]
        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node not in shortest:
                shortest[node] = time
        # then we iterate over the neighbors of that node from the adj list and unpack the node and weight
            # if that nei node does not have a shortest path, we push it to the minHeap (time + neiTime, node).

                for nei, neiTime in adj[node]:
                    if nei not in shortest:
                        heapq.heappush(minHeap, (time + neiTime, nei))
        # once the minHeap is empty we can iterate over the times/weights in shortest and sum that all up and return the total time.
        # if len(shortest) != n, then return -1. 

        return max(shortest.values()) if len(shortest) == n else -1
        
