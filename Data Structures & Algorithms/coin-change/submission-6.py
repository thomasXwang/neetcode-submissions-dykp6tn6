class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')] * (amount + 1) # dp[i] is min nb of coins needed to reach amount i
        dp[0] = 0

        for i in range(amount):
            for coin in coins:
                if i + coin <= amount and dp[i] != -1:
                    dp[i + coin] = min(dp[i + coin], dp[i] + 1)
                    # dp[i + coin] = min(dp[i + coin], dp[i] + 1)
        
        if dp[amount] != float('inf'):
            return dp[amount]
        return -1

            