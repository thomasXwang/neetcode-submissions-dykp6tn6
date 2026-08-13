class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        count = Counter(s)

        res = 0
        hasOdd = False

        for char, freq in count.items():
            print(char, freq)
            if freq % 2 == 0:
                res += freq
            else:
                res += freq - 1
                hasOdd = True

        if hasOdd:
            res += 1

        return res