class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # current = []

        res = []
        
        def backtrack(current, openN, closedN):

            # base case
            if openN == closedN == n:
                complete_string = ''.join(current)
                res.append(complete_string)
                return

            if openN < n:
                backtrack(current + ['('], openN + 1, closedN)

            if closedN < openN:
                backtrack(current + [')'], openN, closedN + 1)

        backtrack([], 0, 0)

        return res