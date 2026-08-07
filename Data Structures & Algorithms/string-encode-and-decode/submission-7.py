class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for word in strs:
            res.append(str(len(word)))
            res.append('#')
            res.append(word)

        return ''.join(res)


    def decode(self, s: str) -> List[str]:
        n = len(s)

        res = []

        i = 0

        while i < n:
            j = 0
            while s[i + j] != '#':
                j += 1
            length = int(s[i:i + j])
            res.append(s[i + j + 1: i + j + 1 + length])
            i = i + j + 1 + length

        return res
