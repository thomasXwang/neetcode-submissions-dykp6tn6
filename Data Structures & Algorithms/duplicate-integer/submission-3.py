class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        from collections import defaultdict

        count = defaultdict(int)

        for i in range(len(nums)):
            count[nums[i]] += 1
            print(f"{nums[i]}: {count[nums[i]]}")
            if count[nums[i]] > 1:
                return True
        return False
