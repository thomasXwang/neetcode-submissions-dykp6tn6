class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        
        summ = sum(nums)
        
        if summ % 2 == 1:
            return False

        target = summ // 2

        cache = dict()

        def dfs(i, remaining):
            if remaining == 0:
                return True

            elif i == n:
                return False

            elif (i, remaining) in cache:
                return cache[(i, remaining)]

            res = dfs(i + 1, remaining) or dfs(i + 1, remaining - nums[i])            
            cache[(i, remaining)] = res
            return res

        return dfs(0, target)