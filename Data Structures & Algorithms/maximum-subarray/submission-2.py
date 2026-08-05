class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        res = float('-inf')

        # optimization: O(1) in space
        # we now compute prefix sum as we go, not all at once
        # we comment out the following lines
        '''
        prefixSum = [0] * (n + 1)

        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]
        '''
        prefixSum = 0
        minPrev = 0
        
        for i in range(1, n + 1):
            prefixSum = prefixSum + nums[i - 1]
            res = max(res, prefixSum - minPrev)
            minPrev = min(minPrev, prefixSum)

        return res