class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [(0, 0)] * (n + 1)   
        # dp[i] = (min product, max product) of subarrays ending at :i
        dp[1] = (nums[0], nums[0])

        for i in range(1, n):
            dp[i + 1] = [
                min(nums[i], dp[i][0] * nums[i], dp[i][1] * nums[i]),
                max(nums[i], dp[i][0] * nums[i], dp[i][1] * nums[i])
            ]

        return max([dp[i][1] for i in range(1, n + 1)])

