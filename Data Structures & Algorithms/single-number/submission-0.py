class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0     # bc n^0 = n for any value n

        for num in nums:
            res = num ^ res

        return res