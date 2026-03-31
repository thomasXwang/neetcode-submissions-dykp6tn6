class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxP = nums[0]
        n = len(nums)

        for l in range(n):
            r = l
            prod = 1
            while r < n:
                prod = prod * nums[r]
                maxP = max(maxP, prod)
                r += 1

        return maxP