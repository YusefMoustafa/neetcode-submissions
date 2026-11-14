class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # given a grid where 1 is land and 0 is water. 
        # count and return the number of islands
        # an island is made up of adjacent peices of land that is surrounded by water. 
        # we can use dfs when we find a cell with 1, and go deep to find when this island ends. each dfs call represents an island. when we return from dfs we increment our islands
        # define our cols and rows. 
        # iterate over the 2d grid
            # for each cell, we will check if its in bounds
            # if the cell is 1 and univisited, then we will call dfs on this cell
        # when dfs returns, increment islands by 1. 

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        neighbors = [[1,0], [-1,0], [0,1], [0,-1]]
        islands = 0
    
        # define dfs function. pass in cell coordinates and visited set. we will return when there are no more adjacent 1's (meaning the island ends).
        # check the cells coordiantes to see if their out of bounds or if the cell has alr been visited or if the cell is 0. if so return.

        # otherwise, check its neighbors to see if the island continues. 
            # call dfs on each neighbor.

        def dfs(r,c):
            if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == '0' or (r,c) in visited:
                return
            visited.add((r,c))
            for nr, nc in neighbors:
                neiR, neiC = nr + r, nc + c
                dfs(neiR, neiC)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r,c)
                    islands += 1
        return islands
        