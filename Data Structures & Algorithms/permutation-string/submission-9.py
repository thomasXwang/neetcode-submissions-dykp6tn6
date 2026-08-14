class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)

        if l2 < l1:
            return False

        c1 = [0] * 26
        for c in s1:
            c1[ord(c) - ord('a')] += 1

        c2 = [0] * 26
        for i in range(l1):
            c2[ord(s2[i]) - ord('a')] += 1

        if c1 == c2:
            return True

        for i in range(l1, l2):
            char = s2[i]
            c2[ord(char) - ord('a')] += 1
            c2[ord(s2[i - l1]) - ord('a')] -= 1

            if c1 == c2:
                return True

        return False