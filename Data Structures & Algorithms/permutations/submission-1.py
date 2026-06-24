class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        used = [False] * n

        res = []

        def dfs(curr):

            if len(curr) == n:
                res.append(curr.copy())
                return

            for i, num in enumerate(nums):
                if not used[i]:
                    curr.append(num)
                    used[i] = True
                    dfs(curr.copy())
                    curr.pop()
                    used[i] = False

        dfs([])

        return res