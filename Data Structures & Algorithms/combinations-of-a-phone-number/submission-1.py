class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        n = len(digits)        
        res = []

        alphabet = ''.join([chr(i) for i in range(ord('a'), ord('a') + 26)])
        # print(alphabet)

        digitToChar = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }

        def dfs(curr, i):
            if i >= n:
                if curr:
                    res.append(curr)
                return

            digit = int(digits[i])
            for char in digitToChar[digit]:
                curr = curr + char
                dfs(curr, i + 1)
                curr = curr[:-1]

        dfs('', 0)

        return res