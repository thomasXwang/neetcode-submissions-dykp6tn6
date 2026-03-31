class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set('+-*/')

        stack = []

        nb = 0

        for c in tokens:
            if c in operators:
                nb = stack.pop()
                prev = stack.pop()

                if c == '+':
                    new = prev + nb
                elif c == '-':
                    new = prev - nb
                elif c == '*':
                    new = prev * nb
                elif c == '/':
                    new = int(prev / nb)
                stack.append(new)

            else:
                nb = int(c)
                stack.append(nb)

            # print(stack)

        return stack[0]

            

