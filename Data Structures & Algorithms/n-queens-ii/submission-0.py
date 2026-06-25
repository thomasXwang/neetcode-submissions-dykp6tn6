class Solution:
    def totalNQueens(self, n: int) -> int:
        
        res = 0

        cols = set()
        diags1 = set()
        diags2 = set()

        def dfs(r):
            nonlocal res

            if r == n:
                res += 1
                return

            for c in range(n):
                if (
                    c in cols or
                    r + c in diags1 or
                    r - c in diags2
                ):
                    continue
                
                cols.add(c)
                diags1.add(r + c)
                diags2.add(r - c)

                dfs(r + 1)

                cols.remove(c)
                diags1.remove(r + c)
                diags2.remove(r - c)

        
        dfs(0)

        return res