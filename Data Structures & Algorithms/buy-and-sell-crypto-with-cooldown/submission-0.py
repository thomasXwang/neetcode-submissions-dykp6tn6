class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        dp = {}

        def dfs(i, holding):
            if i >= n:
                return 0

            if (i, holding) in dp:
                return dp[(i, holding)]

            if holding:
                sell = prices[i] + dfs(i + 2, False)
                hold = dfs(i + 1, True)
                res = max(sell, hold)
            
            else:
                buy = -prices[i] + dfs(i + 1, True)
                skip = dfs(i + 1, False)
                res = max(buy, skip)

            dp[(i, holding)] = res
            return res

        return dfs(0, False)