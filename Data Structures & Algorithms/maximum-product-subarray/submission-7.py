class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)

        currMin = 1
        currMax = 1

        for n in nums:
            if n == 0:
                currMin = 1
                currMax = 1
                continue

            tempMax = max(n * currMax, n * currMin, n)
            currMin = min(n * currMax, n * currMin, n)
            currMax = tempMax

            res = max(res, currMax)

        return res