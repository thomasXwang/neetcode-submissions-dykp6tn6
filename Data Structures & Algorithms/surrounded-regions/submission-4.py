class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS, COLS = len(board), len(board[0])

        def traverse(r, c):
            if not (0 <= r < ROWS and 0 <= c < COLS) or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            traverse(r - 1, c)
            traverse(r + 1, c)
            traverse(r, c - 1)
            traverse(r, c + 1)
        
        # traverse from boudary O's, mark all traversed Os as T
        for r in range(ROWS):
            for c in range(COLS):
                if r in [0, ROWS - 1] or c in [0, COLS - 1] and board[r][c] == 'O':
                    traverse(r, c)

        # mark remaining non-traversed O as X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        # mark T as O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
        