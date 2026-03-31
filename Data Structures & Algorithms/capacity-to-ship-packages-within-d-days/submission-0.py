class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def feasible(capacity):
            time = 1
            load = 0
            for weight in weights:
                load += weight
                if load > capacity:
                    time += 1
                    load = weight
                    if time > days:
                        return False
            return True

        
        # binary search
        l = max(weights)
        r = sum(weights)

        while l < r:
            m = (l + r) // 2
            if feasible(m):
                r = m
            else:
                l = m + 1

        return l