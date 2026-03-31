class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        p = len(s)
        q = len(t)

        countT = defaultdict(int)
        for char in t:
            countT[char] += 1
        need = len(countT)

        minLen = float('inf')
        res = (-1, -1)

        countS = defaultdict(int)
        have = 0

        l = 0
        r = q - 1
        
        for r in range(p):
            char = s[r]
            countS[char] += 1
            if countS[char] == countT[char]:
                have += 1
            
            while have == need:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    res = (l, r)
                
                char = s[l]
                countS[char] -= 1
                if countS[char] < countT[char]:
                    have -= 1
                l += 1

        if res == (-1, -1):
            return ''

        l, r = res
        return s[l: r + 1]

