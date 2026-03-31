class Solution:
    def isPalindrome(self, s: str) -> bool:

        # s = ''.join(filter(str.isalnum, s))
        s = ''.join(filter(self.isalphanum, s))
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

    def isalphanum(self, char):
        return (ord('a') <= ord(char) <= ord('z') or 
                ord('A') <= ord(char) <= ord('Z') or 
                ord('0') <= ord(char) <= ord('9') )