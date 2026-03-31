class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        def overlap(l1, l2):
            if l1[0] <= l2[1] and l2[0] <= l1[1]:
                return True
            return False

        def merge(l1, l2):
            return [min(l1[0], l2[0]), max(l1[1], l2[1])]

        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                res += intervals[i:]
                return res

            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]), 
                    max(newInterval[1], intervals[i][1])
                ]

        res.append(newInterval)

        return res

        