class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # iterate over grid once and process all the treasure chest into a queue
        # while q is not empty, we will iterate over length of q at that time and pop the leftmost from q. 
        # we now will iterate over the cells neighbors, and for each neighbor we will check if that cell is valid (in bounds and a land cell), if so we add it to the queue and a seen set so we dont iterate over twice. and then we change val in place to the distance from treasure. 

        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        seen = set()
        q = deque()
        distance = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    seen.add((r,c))
    
        while q:
            for i in range(len(q)):
                (r,c) = q.popleft()

                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if (min(row,col) < 0 or row == rows or
                        col == cols or (row,col) in seen or grid[row][col] == -1):
                        continue
                    q.append((row,col))
                    seen.add((row,col))
                    grid[row][col] = distance + 1
            
            distance += 1



