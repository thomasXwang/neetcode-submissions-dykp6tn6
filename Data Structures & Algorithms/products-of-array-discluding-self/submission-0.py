class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1 for num in nums]

        for i, num in enumerate(nums):
            for j in range(len(nums)):
                if j != i:
                    result[j] = result[j] * num
        return result