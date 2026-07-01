class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        numSet = set([num for num in nums if num > 0])

        n = len(numSet)

        for num in range(1, n + 2):
            if num not in numSet:
                return num
        