class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            row = board[i]
            count = defaultdict(int)
            for j in range(9):
                if row[j] != '.':
                    if row[j] not in count:
                        count[row[j]] += 1
                    else:
                        return False

        for j in range(9):
            col = [board[i][j] for i in range(9)]
            count = defaultdict(int)
            for i in range(9):
                if col[i] != '.':
                    if col[i] not in count:
                        count[col[i]] += 1
                    else:
                        return False

        for row_start in range(0, 9, 3):
            for col_start in range(0,9,3):
                count = defaultdict(int)
                for i in range(3):
                    for j in range(3):
                        if board[row_start+i][col_start+j] != '.':
                            if board[row_start+i][col_start+j] in count:
                                return False
                            count[ board[row_start+i][col_start+j] ] += 1
        
        return True
            