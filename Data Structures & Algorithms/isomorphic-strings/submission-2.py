class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s2t = dict()
        t2s = dict()

        for i in range(len(s)):

            if s[i] in s2t and t[i] in t2s:
                if s2t[s[i]] != t[i] or t2s[t[i]] != s[i]:
                    return False

            if (
                s[i] in s2t and t[i] not in t2s
            ):
                return False
            if (
                s[i] not in s2t and t[i] in t2s
            ):
                return False

            s2t[s[i]] = t[i]
            t2s[t[i]] = s[i]


        return True