class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)

        cache = {}

        def dfs(i): # return nb of ways of decoding for nums[i:]
            if i == n:
                return 1

            if i > n:
                return 0

            if i in cache:
                return cache[i]

            res = 0
            if s[i] == '0':
                return 0

            res += dfs(i + 1)

            if 1 <= int(s[i: i + 2]) <= 26:
                res += dfs(i + 2)
                
            cache[i] = res
            return res
            
        return dfs(0)
