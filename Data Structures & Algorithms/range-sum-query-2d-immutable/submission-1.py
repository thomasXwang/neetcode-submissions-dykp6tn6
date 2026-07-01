class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])

        self.mat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        # 1st pass: col by col prefix from left to right
        for r in range(ROWS):
            for c in range(COLS):
                self.mat[r + 1][c + 1] = self.mat[r + 1][c] + matrix[r][c]

        # 2nd pass: row by row prefix from top to bottom
        for c in range(COLS):
            for r in range(ROWS):
                self.mat[r + 1][c + 1] = self.mat[r + 1][c + 1] + self.mat[r][c + 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        return (
            self.mat[row2 + 1][col2 + 1]
             - self.mat[row1][col2 + 1]  
             - self.mat[row2 + 1][col1] 
             + self.mat[row1][col1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)