class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0

        maxLen = 0

        for i in range(len(s)):
            seen = {}
            for j in range(i, len(s)):
                # print(seen)
                if s[j] in seen:
                    break
                else:
                    maxLen = max(maxLen, j-i+1)
                    seen[s[j]] = 1
        return maxLen