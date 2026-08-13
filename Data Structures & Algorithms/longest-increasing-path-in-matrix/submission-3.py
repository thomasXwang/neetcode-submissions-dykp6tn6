class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        dirs = (
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        )

        lengths = dict()

        longest = 1

        def dfs(r, c):

            if not (0 <= r < ROWS and 0 <= c < COLS):
                return 0

            if (r, c) in lengths:
                return lengths[(r, c)]

            maxx = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and
                    matrix[nr][nc] > matrix[r][c]
                ):
                    maxx = max(maxx, dfs(r + dr, c + dc))

            lengths[(r, c)] = 1 + maxx
            return lengths[(r, c)]


        for r in range(ROWS):
            for c in range(COLS):
                longest = max(longest, dfs(r, c))
        return longest