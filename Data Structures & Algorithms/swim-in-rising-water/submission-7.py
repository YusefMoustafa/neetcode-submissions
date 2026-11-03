class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # given grid of ints where grid[i][j] == elevation of that cell.
        # we want to find the min of the max amount of time for a path to get from top left to bottom right cell.

        # we can use dijkstra in order to to find the min time path since it utalized a priority queue (minHeap). when we add our nei cells to the heap we will be taking the max elevation of that cell and the nei cell in order to keep track of the highest elevation and then minimize which path has the least of the max using that minHeap. 

        # initialize dimensions of grid, neighbors arr, minHeap, visit set
        ROWS = len(grid)
        COLS = len(grid[0])
        neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        minHeap = [[grid[0][0],0,0]] # [[elev, r, c]]

        # while our minHeap is non empty, we pop off the min elevation cell
            # we check if this cell is alr in visit, continue. if not add it.
            # we check if this cell's coordinates == the bottom right. 
                # if so return its elevation.
        while minHeap:
            elev, r, c = heapq.heappop(minHeap)
            if (r,c) == (ROWS-1,COLS-1):
                return elev
                
            # now we will check its neighbors
                # make sure the nei cell is not out of bounds
                # push the valid nei cells to the minHeap
                    # we push the max(elevation, neiElevation, neiR, neiC)
            
            for nr, nc in neighbors:
                neiR, neiC = nr+r, nc+c
                if min(neiR, neiC) < 0 or neiR == ROWS or neiC == COLS or (neiR,neiC) in visited:
                    continue
                visited.add((neiR, neiC))
                heapq.heappush(minHeap, [max(elev, grid[neiR][neiC]), neiR, neiC])