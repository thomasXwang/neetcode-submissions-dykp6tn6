class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)

        maxRes = float('-inf')
        maxIndex = -1
        res = []

        l = 0 
        for l in range(0, n - k + 1):
            
            maxRes = max(nums[l:l+k])
            res.append(maxRes)
                
        return res

