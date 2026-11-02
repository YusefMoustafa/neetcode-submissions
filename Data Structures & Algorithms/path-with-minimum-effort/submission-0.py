class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        # given heights, 2d array of size rows x cols where heights[row][col] represents the height of a cell (row,col). 
        # from the top left we want to traverse to the bottom right cell.
        # the route must be min effort, meaning the maximum difference of height of 2 adjacent nodes.
        # return the min effort required to do this traversal.

        # we can use dijkstra since that will allow us to find the min effort on a weighted graph where the weight here will be the minimized height. 
        # initialize our dimensions and directions that we can traverse to (left, right, up, down), and a visited set to store cells that weve seen already to avoid infinite loops.
        ROWS = len(heights)
        COLS = len(heights[0])
        neighbors = [[0,1], [0,-1], [1,0], [-1,0]]
        visited = set()
        # initialize a minHeap with the first node in it intially along with its difference which is 0. so (diff, row, col)
        minHeap = [[0,0,0]]
        # while our minHeap is nonempty, well pop off the the cell with smallest effort and check if it is the bottom right cell. if so return the effort. 
            # then we iterate over that cells neighbors and make sure its in bounds by checking if it went out the upper/lower and sides bounds. 
            # take the max of the cells effort and the neighbors effort. that gets pushed to the priority queue (minHeap).

        while minHeap:
            effort, r, c = heapq.heappop(minHeap)
            if (r,c) in visited:
                continue
            visited.add((r,c))
            
            if (r,c) == (ROWS-1,COLS-1):
                return effort
            
            for nr, nc in neighbors:
                newR, newC = r+nr, c+nc
                if newR == ROWS or newC == COLS or min(newR,newC) < 0:
                    continue
                
                newEffort = max(effort, abs((heights[r][c] - heights[newR][newC])))
                heapq.heappush(minHeap, [newEffort, newR, newC])








