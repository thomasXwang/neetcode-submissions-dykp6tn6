class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)

        maxLen = 0

        count = defaultdict(int)

        l = 0

        for r in range(n):
            char = s[r]

            count[char] += 1

            while max(count.values()) + k < r - l + 1:
                count[s[l]] -= 1
                l += 1

            maxLen = max(maxLen, r - l + 1)

        return maxLen