class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = []
        
        for i, char in enumerate(strs[0]):

            for word in strs[1:]:

                if i >= len(word):
                    return ''.join(res)

                if word[i] != char:
                    return ''.join(res)

            res.append(char)


        return ''.join(res)