class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        zeroFirstRow = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r == 0:
                        zeroFirstRow = True
                    else:
                        matrix[r][0] = 0
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # 1st column
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # 1st row
        if zeroFirstRow:
            for c in range(COLS):
                matrix[0][c] = 0
