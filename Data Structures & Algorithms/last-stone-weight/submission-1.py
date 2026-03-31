class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # heap containing - stones to make it able to retrieve max
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        print(maxHeap)

        while len(maxHeap) > 1:
            x = - heapq.heappop(maxHeap)
            y = - heapq.heappop(maxHeap)
            if x > y:
                newStone = x - y
                heapq.heappush(maxHeap, -newStone)

        # print(maxHeap)
        if not maxHeap:
            return 0
        return - maxHeap[0]

