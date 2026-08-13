class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        maxL = height[0]
        maxR = height[-1]

        l = 0
        r = n - 1

        res = 0

        while l < r:

            if maxL < maxR:
                l += 1
                if height[l] > maxL:
                    water = 0
                else:
                    water = maxL - height[l]
                maxL = max(maxL, height[l])

            else:
                r -= 1
                if height[r] > maxR:
                    water = 0
                else:
                    water = maxR - height[r]
                maxR = max(maxR, height[r])

            res += water

        return res