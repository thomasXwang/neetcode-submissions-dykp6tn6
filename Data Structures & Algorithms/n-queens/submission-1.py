class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        
        cols = set()
        posDiag = set()    # (r + c)
        negDiag = set()     # (r - c)

        def backtrack(r):
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return

            # Trying all possible columns in current row
            for c in range(n):
                if (
                    c in cols or
                    (r + c) in posDiag or
                    (r - c) in negDiag
                ):
                    continue
                
                # mark as visited
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = 'Q'

                backtrack(r + 1)
                # backtrack
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = '.'
            
        backtrack(0)

        return res


        