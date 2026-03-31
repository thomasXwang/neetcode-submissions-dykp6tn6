class Solution:
    def partition(self, s: str) -> List[List[str]]:

        n = len(s)
        
        res = []

        def dfs(curr, i):
            if i == n:
                res.append(curr.copy())
                return

            for j in range(i, n):
                if isPali(s, i, j):
                    curr.append(s[i:j+1])
                    dfs(curr, j+1)
                    curr.pop()


        def isPali(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        dfs([], 0)
        return res