"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if len(intervals) == 0:
            return True

        intervals.sort(key = lambda x: x.start)

        prevEnd = intervals[0].end

        for interval in intervals[1:]:
            
            # if overlap, return False
            if interval.start < prevEnd:
                return False
            
            # if no overlap
            else:
                prevEnd = interval.end

        return True