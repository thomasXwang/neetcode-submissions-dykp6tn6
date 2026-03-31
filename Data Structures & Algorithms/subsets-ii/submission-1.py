class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        res = []

        def dfs(curr, i):
            if i >= len(nums):
                # if len(res) > 0 and curr != res[-1]:
                res.append(curr.copy())
                return

            # subsets that include nums[i]
            curr.append(nums[i])
            dfs(curr, i + 1)
            curr.pop()
            # subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            dfs(curr, i + 1)

        dfs([], 0)
        return [list(s) for s in res]
        