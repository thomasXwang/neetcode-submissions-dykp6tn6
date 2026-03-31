class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 1:
            return [[nums[0]]]

        perms = self.permute(nums[1:])
        new_perms = []

        n = len(nums[1:])

        for perm in perms:
            for i in range(n + 1):
                perm_copy = perm.copy()
                perm_copy.insert(i, nums[0])
                new_perms.append(perm_copy)

        return new_perms
        