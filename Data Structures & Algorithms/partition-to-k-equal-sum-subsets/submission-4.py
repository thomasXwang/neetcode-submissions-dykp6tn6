class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)

        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k

        nums.sort(reverse=True)
        if nums[0] > target:
            return False

        subsets = [0] * k

        def dfs(i):
            if i == n:
                return True

            seen_subset_sums = set()

            for j in range(k):
                if subsets[j] in seen_subset_sums:
                    continue
                
                seen_subset_sums.add(subsets[j])

                if subsets[j] + nums[i] <= target:
                    subsets[j] += nums[i]
                    if dfs(i + 1):
                        return True
                    subsets[j] -= nums[i]

            return False

        return dfs(0)