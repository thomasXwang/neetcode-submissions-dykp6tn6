class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        m = len(matrix)
        n = len(matrix[0])

        visited = set()
        res = []

        r, c = 0, 0
        res.append(matrix[r][c])
        visited.add((r, c))

        dir = 0

        for i in range(0, m * n - 1):
            # print(f'r={r}, c={c}')
            dr, dc = directions[dir]
            nr, nc = r + dr, c + dc
            # print(f'nr={nr}, nc={nc}')
            # print(f'dir={dir}')
            if (nr, nc) in visited or not(0 <= nr < m) or not (0 <= nc < n):
                dir = (dir + 1) % 4
            # print(f'dir={dir}')
            dr, dc = directions[dir]
            r = r + dr
            c = c + dc
            # print(dir)
            # print(r, c)
            res.append(matrix[r][c])
            visited.add((r, c))
            # print('-')

        return res


