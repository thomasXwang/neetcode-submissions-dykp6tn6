class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        print(s)

        m = 0
        n = len(s)-1

        while m < n:
            if s[m] != s[n]:
                return False
            m +=1
            n -=1

        return True