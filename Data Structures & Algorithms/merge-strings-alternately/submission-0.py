class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        res = []

        m = len(word1)
        n = len(word2)

        i = 0

        while i < m or i < n:
            a = word1[i] if i < m else ''
            b = word2[i] if i < n else ''

            res.append(a)
            res.append(b)

            i += 1
        
        return ''.join(res)