class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        minRes = float('inf')

        l = 0
        summ = 0

        for r in range(n):
            summ += nums[r]

            while summ >= target:
                minRes = min(minRes, r - l + 1)
                summ -= nums[l]
                l += 1

        if minRes == float('inf'):
            return 0
        return minRes