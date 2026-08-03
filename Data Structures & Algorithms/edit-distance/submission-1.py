class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        p = len(word1)
        q = len(word2)

        # dp[i][j] = edit distance between word1[i:] and word2[j:]
        dp = [[0] * (q + 1) for _ in range(p + 1)]

        # Convert empty word1 suffix into word2[j:]
        for j in range(q + 1):
            dp[p][j] = q - j
        # Convert word1[i:] into empty word2 suffix
        for i in range(p + 1):
            dp[i][q] = p - i

        for i in range(p - 1, - 1, -1):
            for j in range(q - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i + 1][j],
                        dp[i][j + 1],
                        dp[i + 1][j + 1]
                    )
        return dp[0][0]

