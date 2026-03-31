class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0

        for i in range(len(prices)-1):
            j = i+1
            print(prices)
            print(j)
            max_price = prices[j]
            while j < len(prices):
                max_price = max(max_price, prices[j])
                j += 1
            res = max(res, max_price-prices[i])
            print(i, res)
        return res