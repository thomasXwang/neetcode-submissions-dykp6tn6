class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        nums = numbers

        l = 0
        r = len(numbers) - 1

        while l < r:
            print(l, r)
            curSum = nums[l] + nums[r]
            if curSum > target:
                r -= 1
                print(l, r)
            elif curSum < target:
                l += 1
                print(l, r)
            else:
                return [l+1, r+1]