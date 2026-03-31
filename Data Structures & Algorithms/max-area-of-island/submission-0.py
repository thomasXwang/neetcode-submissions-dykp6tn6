class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        maxArea = 0

        def dfs(r, c, area):
            if grid[r][c] == 0:
                return 0

            res = 1
            
            grid[r][c] = '0'
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < ROWS and 
                    0 <= nc < COLS and 
                    grid[nr][nc] == 1
                ):
                    area = dfs(nr, nc, area + 1)

            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    area = dfs(r, c, 1)
                    maxArea = max(maxArea, area)
        
        return maxArea
