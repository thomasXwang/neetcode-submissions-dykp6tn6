class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ''

        delimiter = '#'

        for string in strs:
            res = res + f'{len(string)}' + delimiter + string
        return res

    def decode(self, s: str) -> List[str]:

        res = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            i = j + 1
            j = i + length

            string = s[i: j]
            res.append(string)

            i = j

        return res