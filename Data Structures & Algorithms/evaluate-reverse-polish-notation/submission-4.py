class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)
        }

        for string in tokens:
            if string in '+-*/':
                b = stack.pop()
                a = stack.pop()
                res = operators[string](a, b)
                print(res)
                stack.append(res)
            else:
                stack.append(int(string))

        return stack[-1]