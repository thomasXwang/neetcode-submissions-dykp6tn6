class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        n = len(hand)
        if n % groupSize != 0:
            return False

        count = Counter(hand)

        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            start = minH[0]
            for i in range(start, start+groupSize):
                if count[i] <= 0:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i == minH[0]:
                        heapq.heappop(minH)

        return True