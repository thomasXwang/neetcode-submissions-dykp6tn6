class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        INF = 2**31 - 1
        
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        distance = 0

        while q:
            qLen = len(q)
            distance += 1
            for i in range(qLen):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < ROWS and 
                        0 <= nc < COLS and 
                        grid[nr][nc] == INF
                    ):
                        grid[nr][nc] = distance
                        q.append((nr, nc))
        
