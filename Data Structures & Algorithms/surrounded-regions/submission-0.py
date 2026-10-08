class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows = len(board)
        cols = len(board[0])
        neighbors = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(r,c):
            if r == rows or c == cols or r < 0 or c < 0 or board[r][c] != 'O':
                return

            board[r][c] = 'T'
            for nr, nc in neighbors:
                dfs(r+nr, c+nc)
            
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                    dfs(r,c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
        

