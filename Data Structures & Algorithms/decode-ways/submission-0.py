class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)

        # edge cases: empty string or non-OK first number
        if n == 0 or s[0] == '0':
            return 0

        # dp[i] is number of decoding possibilities of first i characters
        dp = [0] * (n + 1)

        dp[0] = 1   # decoding 0 character: 1 possibility
        dp[1] = 1   # decoding 1 character: 1 possibility

        for i in range(2, n + 1):
            
            # if last index can be decoded alone (ie not 0)
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            # if last 2 indices are valid, then we have dp[i-2] possibilities to decode previous part
            double_int = int(s[i-2:i])
            if 10 <= double_int <= 26:
                dp[i] += dp[i-2]

        return dp[n]
