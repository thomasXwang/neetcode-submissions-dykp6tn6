class Solution:

    def encode(self, strs: List[str]) -> str:
       
        res = ''
        print(strs)
        for string in strs:
            print(string)
            res = res + f'{len(string)}' + '#' + string
        print(res)
        return res

    def decode(self, s: str) -> List[str]:

        res = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            string = s[j+1: j+1+length]

            i = j + length + 1

            res.append(string)

        return res