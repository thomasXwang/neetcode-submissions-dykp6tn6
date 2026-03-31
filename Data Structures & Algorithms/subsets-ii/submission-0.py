class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        res = set()

        def dfs(curr, i):
            if i >= len(nums):
                # if len(res) > 0 and curr != res[-1]:
                res.add(tuple(curr))
                return

            dfs(curr, i + 1)
            curr.append(nums[i])
            dfs(curr, i + 1)
            curr.pop()

        dfs([], 0)
        return [list(s) for s in res]
        