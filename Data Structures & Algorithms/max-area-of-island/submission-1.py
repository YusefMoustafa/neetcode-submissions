class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        # use recursive dfs to go as deep as possible to find all islands. 
        # define neighbors, rows, cols, visited, maxIsland
        # define helper function that will check if vertex's neighbors are valid
            #checking bounds of r,c and if (r,c) in visited and if val == 0
            # if valid, iterate over neighbors and call dfs(r+nr, c+nc).
        # we will iterate over entire search space
    
            # for each valid vertex (has val of 1 and hasnt been visited before), we will recursively check its neighbors.

            # maxIsland = max(maxIsland, currIsland)
            # return maxIsland

        rows = len(grid)
        cols = len(grid[0])
        neighbors = [[-1,0], [1,0], [0,-1], [0,1]]
        visited = set()
        maxIsland = 0
        

        def dfs(r,c):
            if min(r,c) < 0 or r == rows or c == cols or (r,c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r,c))
            area = 1

            for nr, nc in neighbors:
                area += dfs(r+nr, c+nc)
            
            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxIsland = max(maxIsland, dfs(r,c))
        return maxIsland


