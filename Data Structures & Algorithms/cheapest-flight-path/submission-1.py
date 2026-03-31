class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        INF = float('inf')

        prices = [INF] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()   # what we're updating
            for s, d, price in flights:
                if prices[s] != INF:
                    tmpPrices[d] = min(tmpPrices[d], prices[s] + price)
            prices = tmpPrices

        if prices[dst] == INF:
            return -1
        return prices[dst]