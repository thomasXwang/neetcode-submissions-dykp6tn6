class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for string in strs:
            res = res + str(len(string)) + '#' + string
        return res


    def decode(self, s: str) -> List[str]:

        res = []

        i = 0
        while i < len(s):
            num_start_idx = i
            while s[i].isdigit():
                i += 1
            seq_length = int(s[num_start_idx: i])

            res.append( s[i+1: i+1+seq_length] )
            i = i + seq_length + 1
        
        return res




