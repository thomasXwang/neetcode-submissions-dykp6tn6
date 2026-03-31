class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        n = len(nums)
        
        l = 0
        r = n       # already nums[n] doesnt exist
        
        while l < r:
            m = (l + r) // 2
            # print(l, r, m)
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        
        return l
