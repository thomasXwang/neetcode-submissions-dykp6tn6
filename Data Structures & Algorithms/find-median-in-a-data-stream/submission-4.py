class MedianFinder:

    def __init__(self):
        self.len = 0
        self.nums = []
        self.mid = 0
        

    def addNum(self, num: int) -> None:
        i = 0
        while i < self.len and num < self.nums[i]:
            i += 1
        self.nums = self.nums[:i] + [num] + self.nums[i:]
        
        self.len += 1
        

    def findMedian(self) -> float:
        print(self.nums)
        if self.len == 0:
            mid = None
        if self.len == 1:
            mid = self.nums[0]
        else:
            mid1 = (self.len - 1) // 2
            mid2 = self.len // 2
            print(mid1)
            print(mid2)
            print(self.nums[mid1])
            print(self.nums[mid2])
            mid = ( self.nums[mid1] + self.nums[mid2] ) / 2
            print(f'mid: {mid}')
        return mid


        