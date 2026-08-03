class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        # dp[rest] is # of ways to sum up to rest using coins in coins[i:]
        # i is the # of times we iterate over rest
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(n - 1, -1, -1):
            coin = coins[i]

            for rest in range(coin, amount + 1):
                # dp[i][rest] = dp[i + 1][rest] + dp[i][rest - coin]
                dp[rest] = dp[rest] + dp[rest - coin]

        return dp[amount]
