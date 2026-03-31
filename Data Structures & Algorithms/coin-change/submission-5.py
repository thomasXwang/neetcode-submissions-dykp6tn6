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

        # V1: Outer loop on array indices
        # for i in range(1, amount + 1):
        #     for coin in coins:
        #         if coin <= i:
        #             dp[i] = min(dp[i], dp[i - coin] + 1)

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
