class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)

        dp = [1] * n  # dp[i] = length of longest increasing subsequence ending at index i included

        for start in range(n):
            for nxt in range(start + 1, n):
                if nums[nxt] > nums[start]:
                    dp[nxt] = max(dp[nxt], dp[start] + 1)

        return max(dp)