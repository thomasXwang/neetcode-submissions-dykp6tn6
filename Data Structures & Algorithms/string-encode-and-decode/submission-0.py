class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res = res + str(len(s)) + '#' + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # find the end of count integer, indicated by presence of #
            j = i
            while s[j] != '#':
                j += 1
            count = int(s[i:j])
            print(count)
            print(s[j+1:j+1+count])

            res.append( s[j+1:j+1+count] )
            print(res)
            i = j + 1 + count

        return res



