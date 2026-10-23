from collections import defaultdict
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        # build an adjList that maps each stop to list of buses that go there. this way we can check which buses we can transfer to. 
        # {7:[0], 12:[0,4], 4:[1], 5:[1], 15:[1,3], 6:[2], 19:[3], 13:[4]}
        # {1:[0], 2:[0], 7:[0,1], 3:[1], 6:[1]}

        if source == target:
            return 0
        stopToBus = defaultdict(list)

        for bus, stops in enumerate(routes):
            for stop in stops:
                stopToBus[stop].append(bus)
        
        if source not in stopToBus:
            return -1

        # use BFS
        q = deque([source])
        seenStop = set([source])
        seenBus = set()
        res = 0
        while q:
            for i in range(len(q)):
                stop = q.popleft()
                if stop == target:
                    return res
                for bus in stopToBus[stop]:
                    if bus not in seenBus:
                        seenBus.add(bus)
                    
                    for nextStop in routes[bus]:
                        if nextStop not in seenStop:
                            seenStop.add(nextStop)
                            q.append(nextStop)

            res += 1
        return -1

