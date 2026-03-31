class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        nums = numbers

        i = 0
        j = len(numbers) - 1

        while nums[i] + nums[j] != target:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
        return [i+1, j+1]