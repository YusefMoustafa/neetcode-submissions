class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # iterate over the entire grid, when we arrive at a 1, we do a recursive call.
        # the dfs function will establish base cases for when the function is out of bounds or has already been visited or is not 1. 
        # then it will add this cell to our seen set and then dfs into all 4 directions (via for loop)
        # when the dfs call returns due to base case returns, we add 1 to our islands
        # return islands

        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        seen = set()
        islands = 0

        def dfs(r,c):
            if min(r,c) < 0 or r == rows or c == cols or (r,c) in seen or grid[r][c] == '0':
                return 0
            
            seen.add((r,c))

            for dr, dc in directions:
                dfs(r+dr, c+dc)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in seen:
                    dfs(r,c)
                    islands += 1

        return islands