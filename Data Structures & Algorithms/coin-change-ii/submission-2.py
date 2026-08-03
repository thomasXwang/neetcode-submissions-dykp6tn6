class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        cache = {}

        def dfs(i, rest):    # nb of combinations using coins in coins[i:] that total up to rest
            if rest == 0:
                return 1

            if i == n or rest < 0:
                return 0

            if (i, rest) in cache:
                return cache[(i, rest)]

            res = (
                dfs(i, rest - coins[i])
                + dfs(i + 1, rest)
            )
            cache[(i, rest)] = res
            return res

        return dfs(0, amount)
