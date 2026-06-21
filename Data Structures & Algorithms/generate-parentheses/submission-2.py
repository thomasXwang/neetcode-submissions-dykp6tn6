class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def dfs(curr, nOpen, nClose):
            if nOpen == nClose == n:
                res.append(''.join(curr))
                return

            if nOpen < n:
                curr.append('(')
                dfs(curr, nOpen + 1, nClose)
                curr.pop()

            if nOpen > nClose:
                curr.append(')')
                dfs(curr, nOpen, nClose + 1)
                curr.pop()

        dfs([], 0, 0)

        return res