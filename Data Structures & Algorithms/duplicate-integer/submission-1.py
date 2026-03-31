class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashset = set()

        for i, n in enumerate(nums):
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False

         