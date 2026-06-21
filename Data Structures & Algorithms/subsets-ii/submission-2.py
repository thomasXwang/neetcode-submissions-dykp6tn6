class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)

        nums.sort()

        res = []

        def dfs(curr, i):

            if i == n:
                res.append(curr)
                return

            # include nums[i]
            dfs(curr + [nums[i]], i + 1)

            # not include nums[i], then we have to move to the next index that will not have nums[i] value
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            dfs(curr, i + 1)

        
        dfs([], 0)

        return res