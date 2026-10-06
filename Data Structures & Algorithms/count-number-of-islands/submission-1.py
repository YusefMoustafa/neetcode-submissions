class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # define variables
        # loop through entire grid, when we arrive at a non previously visited val and a 1, we run our dfs helper function on it. this will then check all its neighbors for for more land (aka 1's) and add it to our visited set. 
        # must make sure set base cases for dfs function to make sure we add a element that is in bounds, not been prev visited, and is not water (0).
        # add 1 to our islands counter once the dfs call returns back. 
        # return islands


        rows = len(grid)
        cols = len(grid[0])
        neighbors = [[-1,0], [1,0], [0,-1], [0,1]]
        visited = set()
        islands = 0

        def dfs(r,c):
            if r == rows or c == cols or min(r,c) < 0 or grid[r][c] == "0" or (r,c) in visited:
                return
            visited.add((r,c))
            
            for nr, nc in neighbors:
                dfs(r+nr, c+nc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    islands += 1

        return islands
