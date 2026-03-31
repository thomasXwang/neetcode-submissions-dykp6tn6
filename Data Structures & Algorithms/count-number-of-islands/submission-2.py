class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        visited = set()
        islands = 0

        def bfs(r, c):

            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == '1' and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands