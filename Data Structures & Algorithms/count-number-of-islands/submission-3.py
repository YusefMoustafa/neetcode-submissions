class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # solution using explicit stack

        rows, cols = len(grid), len(grid[0])
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        visited = set()
        stack = []
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                     islands += 1
                     visited.add((r,c))
                     stack.append((r,c))

                     while stack:
                        currRow, currCol = stack.pop()

                        for dr, dc in directions:
                            nr = currRow + dr
                            nc = currCol + dc

                            if (min(nr, nc) < 0 or nr == rows or nc == cols
                                or (nr,nc) in visited or grid[nr][nc] == '0'):
                                    continue

                            stack.append((nr,nc))
                            visited.add((nr,nc))
        return islands
