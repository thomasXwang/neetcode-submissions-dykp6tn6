class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        S = sum(nums)

        # nb of ways to sum up to 0 with the first i elements
        dp = [defaultdict(int) for _ in range(n + 1)]

        dp[0][0] = 1    # there's 1 way to sum up to 0 with the first 0 elements

        for i in range(n):
            for curr_sum, count in dp[i].items():
                dp[i + 1][curr_sum + nums[i]] += count
                dp[i + 1][curr_sum - nums[i]] += count

        return dp[n][target]