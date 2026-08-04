class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        S = sum(nums)

        # nb of ways to sum up to 0 with the first i elements
        # dp = [defaultdict(int) for _ in range(n + 1)]
        dp = defaultdict(int)

        # dp[0][0] = 1    # there's 1 way to sum up to 0 with the first 0 elements
        dp[0] = 1

        for i in range(n):
            next_dp = defaultdict(int)
            for curr_sum, count in dp.items():
                next_dp[curr_sum + nums[i]] += count
                next_dp[curr_sum - nums[i]] += count
            dp = next_dp

        # return dp[n][target]
        return dp[target]