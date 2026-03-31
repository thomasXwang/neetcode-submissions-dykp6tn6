class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)

        res = 0

        count = defaultdict(int)
        count[0] = 1
        prefix = 0

        for num in nums:
            prefix += num
            if prefix - k in count:
                res += count[prefix - k]
            count[prefix] += 1

        return res
        