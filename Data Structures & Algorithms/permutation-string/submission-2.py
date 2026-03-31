class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        count1 = Counter(s1)

        count2 = Counter(s2[:n1])

        if count1 == count2:
            return True

        l = 0
        
        for r in range(n1, n2):
            count2[s2[r]] += 1
            count2[s2[l]] -= 1

            l += 1

            if count1 == count2:
                return True

        return False
