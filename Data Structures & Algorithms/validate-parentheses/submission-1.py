class Solution:
    def isValid(self, s: str) -> bool:
        
        right2left = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        rights = set(right2left.keys())
        lefts = set(right2left.values())

        stack = []

        for char in s:
            if char in lefts:
                stack.append(char)
            elif char in rights:
                if stack and stack[-1] == right2left[char]:
                    stack.pop()
                    continue
                else:
                    return False
        if not stack:
            return True
        else:
            return False