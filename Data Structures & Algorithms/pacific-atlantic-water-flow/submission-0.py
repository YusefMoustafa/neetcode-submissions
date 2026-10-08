class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # a cell can reach ocean if water can flow from that cell to the ocean. (<=)
        # realize that if we start from ocean borders, we can move uphill (>=) because if water can flow from the uphill position then it will flood to ocean. 
        # we can do 2 dfs runs. 
        # 1. left and right boundaries (since theyll be same size (rows size)) and call dfs twice. pass in r, c of ocean facing bounds with coresponding ocean set and the mosr prevHeight weve seen to compare against in the dfs function. 
        # 2. top and bottom boundaries since theyll both be same size (cols size) and call dfs twice. pass in r,c of ocean facing bound along with corresponding ocean set and prevHeight. 
        # dfs function will check if cell were on is < prevHeight, if so return. Also base cases if were out of bounds, and if (r,c) in either set. if not add it to set. 

        # call dfs on all neighbors. 

        # iterate over entire search space and if (r,c) in pac and atl then append it to res array. 


        rows = len(heights)
        cols = len(heights[0])
        neighbors = [[1,0], [-1,0], [0,1], [0,-1]]
        pac = set()
        atl = set()


        def dfs(r, c, seen, prevHeight):

            if min(r,c) < 0 or r == rows or c == cols or (r,c) in seen or heights[r][c] < prevHeight:
                return

            seen.add((r,c))

            for nr, nc in neighbors:
                dfs(r+nr, c+nc, seen, heights[r][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])

        res = []

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res














