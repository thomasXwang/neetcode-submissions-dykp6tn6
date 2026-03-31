class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l = 0
        r = ROWS * COLS - 1

        while l <= r:
            mid = (l + r) // 2

            row = mid // COLS
            col = mid % COLS
            
            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1

        return False