class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)

        stack = []

        maxArea = 0

        for i, height in enumerate(heights):

            start = i

            while stack and height <= stack[-1][0]:
                prev_height, prev_idx = stack.pop()
                unextendableArea = prev_height * (i - prev_idx)

                maxArea = max(maxArea, unextendableArea)

                start = prev_idx

            stack.append((height, start))

        
        for height, start in stack:
            maxArea = max(maxArea, height * (n - start))

        return maxArea
