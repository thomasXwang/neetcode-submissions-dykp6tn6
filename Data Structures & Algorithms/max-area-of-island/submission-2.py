class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        maxArea = 0

        def dfs(r, c):
            if not(0 <= r < ROWS and 0 <= c < COLS) or grid[r][c] == 0:
                return 0
            
            # mark cell as visited
            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                area += dfs(nr, nc)
            
            return area

        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(maxArea, dfs(r, c))

        return maxArea