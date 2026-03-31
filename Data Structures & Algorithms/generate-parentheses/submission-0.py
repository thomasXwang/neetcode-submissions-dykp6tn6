class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        current = []

        res = []
        
        def backtrack(openN, closedN):

            # base case
            if openN == closedN == n:
                complete_string = ''.join(current)
                res.append(complete_string)
                return

            if openN < n:
                current.append('(')
                backtrack(openN + 1, closedN)
                current.pop()

            if closedN < openN:
                current.append(')')
                backtrack(openN, closedN + 1)
                current.pop()


        backtrack(0, 0)

        return res