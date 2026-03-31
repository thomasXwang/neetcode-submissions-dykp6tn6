class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x: x[0])

        res = [intervals[0]]

        for start, end in intervals[1:]:
            
            # if overlap with prev window, the merge with previous interval
            if start <= res[-1][1]:
                res[-1][1] = max(end, res[-1][1])

            # if no overlap
            else:
                res.append([start, end])

        return res