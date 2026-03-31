class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        
        # XOR operator

        res = n
        for i, num in enumerate(nums):
            res = res ^ i ^ num

        return res