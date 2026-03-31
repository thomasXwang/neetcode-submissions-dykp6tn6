"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        starts = sorted( [i.start for i in intervals] )
        ends = sorted( [i.end for i in intervals] )
        
        
        res = 0
        count = 0
        
        # init 2 pointers
        s = 0
        e = 0

        while s < len(starts):
            # if we have to start a meeting
            if starts[s] < ends[e]:
                count += 1
                res = max(res, count)
                s += 1
            
            # if we have to end a meeting (edge case of start==end is done via first ending a meeting)
            else:
                count -= 1
                e += 1

        return res

