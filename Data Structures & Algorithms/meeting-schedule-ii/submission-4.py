"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        
        start = sorted([interval.start for interval in intervals])
        end = sorted([interval.end for interval in intervals])

        count = 0
        res = 0

        s = 0   # pointer of interval starts
        e = 0   # pointer of interval ends

        while s < len(intervals):
            # if meeting s starts before meeting e ends
            if start[s] < end[e]:
                count += 1
                s += 1
            # if meeting e ends before meeting s starts
            # if tie: end meeting e before starting s
            else:
                count -= 1
                e += 1
            res = max(res, count)

        return res


