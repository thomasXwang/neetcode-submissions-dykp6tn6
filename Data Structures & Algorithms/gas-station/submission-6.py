class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n = len(gas)

        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0

        # we try all indices
        # as soon as going sum becomes negative, we reset sum to 0 and move to next one
        for i in range(n):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                start = i + 1
        
        return start
