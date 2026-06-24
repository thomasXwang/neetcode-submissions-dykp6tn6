class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)

        nums.sort()

        # used = [False] * len(nums)
        # remaining = nums.copy()

        res = []

        def dfs(curr, remaining):

            if len(curr) == n:
                res.append(curr.copy())
                return

            for i, num in enumerate(remaining):
                if i > 0 and remaining[i] == remaining[i - 1]:
                    continue
                dfs(curr + [num], remaining[:i] + remaining[i + 1:] )
            

        dfs([], nums)

        return res