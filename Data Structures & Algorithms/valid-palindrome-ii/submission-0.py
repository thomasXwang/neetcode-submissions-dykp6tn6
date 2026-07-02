class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        
        l = 0
        r = n - 1

        def isPali(i, j):
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            
            else:
                return isPali(l + 1, r) or isPali(l, r - 1)


        return True