class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: x[0])

        res = 0 # counter
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:

            # if non overlapping, just update latest ending time
            if start >= prevEnd:
                prevEnd = end
            
            # if overlapping, we need to delete 1 interval
            # Which one? The one that will bother us most, ie that ends latest
            else:
                res += 1
                prevEnd = min(prevEnd, end)

        return res