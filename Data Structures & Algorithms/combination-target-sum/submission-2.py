class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(curr, currSum, i):

            if i == len(nums):
                return
            elif currSum > target:
                return
            elif currSum == target:
                res.append(curr)
                return

            dfs(curr + [nums[i]], currSum + nums[i], i)
            dfs(curr, currSum, i + 1)


        dfs([], 0, 0)

        return res