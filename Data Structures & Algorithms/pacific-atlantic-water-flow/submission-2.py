class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(heights)
        COLS = len(heights[0])

        pac = set()
        atl = set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or 
                not (r in range(0, ROWS)) or 
                not (c in range(0, COLS)) or
                heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])


        for c in range(COLS):
            dfs(0, c, pac, 0)
            dfs(ROWS - 1, c, atl, 0)

        for r in range(ROWS):
            dfs(r, 0, pac, 0)
            dfs(r, COLS - 1, atl, 0)


        common = pac & atl
        result_list = [list(item) for item in common]

        return result_list