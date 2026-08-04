class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        cache = {}

        def dfs(i, remaining):

            if i == n:
                if remaining == 0:
                    return 1
                return 0

            if (i, remaining) in cache:
                return cache[(i, remaining)]

            res = (
                dfs(i + 1, remaining - nums[i])
                + dfs(i + 1, remaining + nums[i])
            )
            cache[(i, remaining)] = res
            return res


        return dfs(0, target)