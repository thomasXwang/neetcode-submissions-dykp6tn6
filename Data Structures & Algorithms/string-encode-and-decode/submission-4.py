class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ''

        for word in strs:
            res += str(len(word)) + '#' + word
        
        return res

    def decode(self, s: str) -> List[str]:

        res = []

        i = 0
        count = 0
        while i < len(s):
            if s[i] == '#':
                i += 1
                res.append(s[i:i+count])
                i += count
                count = 0
            elif s[i].isdigit():
                count = 10 * count + int(s[i])
                i += 1
        
        return res
