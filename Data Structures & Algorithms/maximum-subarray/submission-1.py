class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        res = float('-inf')

        prefixSum = [0] * (n + 1)

        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        minPrev = 0
        for i in range(1, n + 1):
            res = max(res, prefixSum[i] - minPrev)
            minPrev = min(minPrev, prefixSum[i])

        return res