class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: x[0])

        res = 0

        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:

            # if non overlap, just move on to the next interval
            if start >= prevEnd:
                prevEnd = end

            # if overlap, remove 1 of the 2: the one that ends later
            else:
                prevEnd = min(prevEnd, end)
                res += 1

        return res