class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n = len(gas)

        tank = [gas[i] - cost[i] for i in range(n)]

        if sum(tank) < 0:
            return -1

        currSum = 0
        i = 0
        start_index = 0
        while i < n:
            currSum += tank[i]
            if currSum < 0:
                currSum = 0
                start_index = i + 1
            i += 1
            
        return start_index