class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # edge cases
        if amount == 0:
            return 0
        if not coins:
            return -1
        
        # init dp array
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i and dp[i - coin] != -1:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
            # if all coins had invalid dp values
            if dp[i] == float('inf'):
                dp[i] = -1

        return dp[amount]

