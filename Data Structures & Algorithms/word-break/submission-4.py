class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        
        dp = [False] * (n + 1)    # dp[i] is can we build s[:i] from the words in the dict
        dp[0] = True

        for i in range(n):
            if dp[i] == True:
                for word in wordDict:
                    # if i + len(word) <= n and word == s[i: i + len(word)]:
                    if s.startswith(word, i):
                        dp[i + len(word)] = True

        return dp[n]

