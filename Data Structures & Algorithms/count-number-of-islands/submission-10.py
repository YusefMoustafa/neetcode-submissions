from collections import deque
class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        
        # given a grid made up of 0's (water) and 1's (land).
        # count and return the # of islands in the grid
        # an island is made up of adjancent blocks of land that are surrounded by water. 
        # dfs and bfs both work since were going to iterate over each cell once. here well do bfs which will require a queue. 

        # initiaize directions, visited set, rows,cols, islands.
        # we will iterate over the grid cell by cell, and when we find unvisited land ('1'), then we call bfs and icnrement islands. 

        # bfs takes in r,c. initialize the queue and append the (r,c). mark this cell as visited. 
        # while queue is nonemepty, were going to pop the left most from it. 
        # iterate over this cells neighbors and check if each nei cell is in bounds and valid. if so add it to the queue. otherwise continue. 

        rows, cols = len(grid), len(grid[0])
        neighbors = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()
        islands = 0


        def bfs(r,c):

            q = deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                r, c = q.popleft()
                for nr, nc in neighbors:
                    neiR, neiC = nr+r, nc+c
                    if min(neiR, neiC) < 0 or neiR == rows or neiC == cols or grid[neiR][neiC] == '0' or (neiR, neiC) in visited:
                        continue
                    q.append((neiR,neiC))
                    visited.add((neiR,neiC))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands