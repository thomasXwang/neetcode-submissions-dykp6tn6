class Solution:
    def isValid(self, s: str) -> bool:
        close2open = {
            ')':'(',
            '}': '{',
            ']': '['
        }
        closed = set(close2open.keys())
        opened = set(close2open.values())
        
        stack = []

        for c in s:
            if c in opened:
                stack.append(c)
            
            elif c in closed:
                if stack and stack[-1] == close2open[c]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0

