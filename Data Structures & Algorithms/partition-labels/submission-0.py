class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        n = len(s)
        
        # count all latest index positions of each character
        lastIndex = dict()
        for i, char in enumerate(s):
            lastIndex[char] = i

        res = []
        # 
        start = 0
        end = 0
        for i, char in enumerate(s):
            end = max(end, lastIndex[char])
            if i == end:
                res.append(end - start + 1)
                start = i + 1

        return res