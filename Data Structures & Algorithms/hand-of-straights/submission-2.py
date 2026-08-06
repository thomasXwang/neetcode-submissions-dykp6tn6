class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n % groupSize != 0:
            return False
        nGroups = n // groupSize

        counts = Counter(hand)
        values = sorted(counts.keys())

        for val in values:

            groups_to_start = counts[val]

            for offset in range(groupSize):
                if counts[val + offset] < groups_to_start:
                    return False
                counts[val + offset] -= groups_to_start

        return True
            

