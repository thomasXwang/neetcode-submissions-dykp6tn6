class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()

        res = []
        n = len(candidates)

        def dfs(curr, i, total):

            if total == target:
                res.append(curr.copy())
                return

            if total > target:
                return
            if i == n:
                return

            # subsets that include candidates[i]
            curr.append(candidates[i])
            dfs(curr, i + 1, total + candidates[i])
            curr.pop()

            # subsets that dont include candidates[i]
            while i + 1 < n and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(curr, i + 1, total)

        dfs([], 0, 0)

        return res