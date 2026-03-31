class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        if endWord == beginWord:
            return 0
        wordList = wordList + [beginWord]

        # change string to patterns
        nei = collections.defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                nei[pattern].append(word)
        
        visit = set([beginWord])
        q = deque([beginWord])

        res = 1

        while q:
            qLen = len(q)
            for i in range(qLen):
                word = q.popleft()
                if word == endWord:
                    return res
                # iterating over all neighbors of word
                ## iterating over patterns
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for neighbor in nei[pattern]:
                        if neighbor not in visit:
                            visit.add(neighbor)
                            q.append(neighbor)
            res += 1
        
        return 0