class MedianFinder:

    def __init__(self):
        # 2 heaps: small (maxheap), large (minheap)
        # heaps should be equal-ish sized
        # max(small) < min(large)
        self.small = []
        self.large = []

        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # make sure that each element in small <= each element in large
        if (self.small and self.large and 
            (-1 * self.small[0]) > self.large[0]
        ):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # uneven sizes?
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # if odd length
        if len(self.small) > len(self.large):
            return (-1) * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return ((-1) * self.small[0] + self.large[0]) / 2
        