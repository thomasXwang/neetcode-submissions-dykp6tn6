class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        count1 = Counter(s1)

        n1 = len(s1)
        n2 = len(s2)

        l = 0 
        r = n1 - 1

        found = True

        count2 = Counter(s2[l:r+1])

        if count1 == count2:
            return True

        for r in range(n1, n2):

            count2[s2[r]] += 1
            count2[s2[l]] -= 1
            l += 1
            if count1 == count2:
                return True

        return False


