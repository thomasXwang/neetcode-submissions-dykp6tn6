class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        import math
        
        n = len(gifts)

        maxHeap = [-g for g in gifts]
        heapq.heapify(maxHeap)

        for i in range(k):
            gifts = - heapq.heappop(maxHeap)
            gifts = math.floor(math.sqrt(gifts))
            heapq.heappush(maxHeap, -gifts)

        return -sum(maxHeap)
