class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        prefix = [1] * (n+1)
        suffix = [1] * (n+1)
        
        for i, num in enumerate(nums):
            prefix[i+1] = num * prefix[i]
            
        for i, num in enumerate(nums[::-1]):
            suffix[-i-2] = num * suffix[-i-1]

        result = [1] * n
        

        print(prefix)
        print(suffix)

        for i in range(n):
            result[i] = prefix[i] * suffix[i+1]

        return result
