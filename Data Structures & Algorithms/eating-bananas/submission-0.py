class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        n = len(piles)
        
        low = 1
        low = math.ceil(sum(piles) / h)
        high = max(piles)

        res = high

        while low <= high:
            mid = (low + high) // 2

            sumHours = sum([math.ceil(piles[i] / mid) for i in range(n)])
            if sumHours > h:
                low = mid + 1
            elif sumHours <= h:
                high = mid - 1
                res = min(res, mid)

        return res


