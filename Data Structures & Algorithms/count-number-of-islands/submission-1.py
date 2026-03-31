class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        ROWS = len(grid)
        COLS = len(grid[0])

        visit = set()

        islands = 0

        def bfs(r, c):

            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            # while q not empty, we pop out from it
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (
                        r in range(ROWS) and \
                        c in range(COLS) and \
                        grid[r][c] == '1' and \
                        (r, c) not in visit
                        ):
                        q.append((r, c))
                        visit.add((r, c))
                


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands
