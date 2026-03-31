class Solution:
    def checkValidString(self, s: str) -> bool:
        
        leftMin = 0 # min left open parenthesis
        leftMax = 0 # max left open parenthesis

        for c in s:
            if c == '(':
                leftMin = leftMin + 1
                leftMax = leftMax + 1
            elif c == ')':
                leftMin = leftMin - 1
                leftMax = leftMax - 1
            else:
                leftMin = leftMin - 1
                leftMax = leftMax + 1
            
            if leftMax < 0:
                return False
            if leftMin < 0: # use s = ( * ) (
                leftMin = 0

        return leftMin == 0