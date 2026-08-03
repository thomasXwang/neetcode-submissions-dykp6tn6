class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        p = len(word1)
        q = len(word2)

        cache = {}

        def dfs(i, j):
            if i == p:
                return q - j

            if j == q:
                return p - i

            if (i, j) in cache:
                return cache[(i, j)]

            if word1[i] == word2[j]:
                res = dfs(i + 1, j + 1)
                cache[(i, j)] = res
                return res

            res = 1 + min(
                dfs(i + 1, j),
                dfs(i, j + 1),
                dfs(i + 1, j + 1)
            )
            cache[(i, j)] = res
            return res

        return dfs(0, 0)
            
