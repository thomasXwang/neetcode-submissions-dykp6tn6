class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0

        minPrev = float('inf')

        for price in prices:
            maxProfit = max(maxProfit, price - minPrev)
            minPrev = min(minPrev, price)

        return maxProfit