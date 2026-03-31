class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)

        res = [0] * n

        # we store the indices of each day so that the stack of corresponding temperatures are the ones of which we're still looking for warmer future day
        stack = []

        for i, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx

            stack.append(i)

        return res