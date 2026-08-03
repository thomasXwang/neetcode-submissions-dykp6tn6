class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        p = len(s)
        q = len(t)

        cache = {}
        
        # dfs(i, j) = # of distinct subsequences of s[i:] that are equal to t[j:]
        def dfs(i, j):

            if j == q:
                return 1
            if i == p:
                return 0

            if (i, j) in cache:
                return cache[(i, j)]
            
            if s[i] == t[j]:
                res = (
                    dfs(i + 1, j + 1)       # we include s[i], then we have to match s[i+1:] with t[j+1:], as t[j] is matched
                    + dfs(i + 1, j)         # we don't include s[i], we just check right-er part to see if it matches
                )

            else:
                res = dfs(i + 1, j)

            cache[(i, j)] = res
            return res

        return dfs(0, 0)

            
