class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        
        wordSet = set(wordDict)

        cache = {}

        def dfs(i):     # return all valid sentences starting from i

            res = []

            if i == n:
                return ['']

            if i in cache:
                return cache[i]
            
            for j in range(i + 1, n + 1):
                w = s[i: j]
                if w in wordSet:
                    print(w, j)
                    for tail in dfs(j):
                        curr = w + ' ' + tail if tail else w
                        res.append(curr)
            cache[i] = res
            return res
                        

        return dfs(0)
            