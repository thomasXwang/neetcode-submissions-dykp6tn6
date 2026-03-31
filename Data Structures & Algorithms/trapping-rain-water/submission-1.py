class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
        
        n = len(height)

        l = 0
        r = n - 1

        leftMax = height[l]
        rightMax = height[r]

        totalArea = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                totalArea += leftMax - height[l]  # always >0 due to prev line
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                totalArea += rightMax - height[r] # always >0 due to prev line
        return totalArea

