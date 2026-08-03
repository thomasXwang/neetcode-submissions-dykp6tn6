class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        cache = {}

        def dfs(curr):

            if len(curr) == 0:
                return 0

            if curr in cache:
                return cache[curr]

            best = 0

            n = len(curr)
            for i in range(n):
                prev = curr[i - 1] if i > 0 else 1
                nxt = curr[i + 1] if i < n - 1 else 1
                num = curr[i]

                remaining = curr[:i] + curr[i + 1:]
                coins = dfs(remaining) + prev * nxt * num

                best = max(best, coins)

            cache[curr] = best
            return best
            
        return dfs(tuple(nums))