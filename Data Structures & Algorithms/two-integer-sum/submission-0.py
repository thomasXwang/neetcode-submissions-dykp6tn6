class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        hashtable = {}

        for index, value in enumerate(nums):
            print(index, value)
            target_value = target-value
            print(target_value)
            print(hashtable)
            if target_value in hashtable:
                return [hashtable[target_value], index]
            else:
                hashtable[value] = index

        