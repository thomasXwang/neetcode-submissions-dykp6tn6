class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # left-half is sorted
            if nums[m] >= nums[l]:
                # we are
                if target > nums[m]:
                    l = m + 1
                elif target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

            # right-half is sorted
            else:
                if target < nums[m]:
                    r = m - 1
                elif target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1

            