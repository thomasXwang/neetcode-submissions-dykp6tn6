class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        if len(words) == 1:
            return words[0]
        
        # Create adjacency lists
        adjacency = defaultdict(list)

        in_degree = {char: 0 for word in words for char in word}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            min_len = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ''
            
            # find index where they begin to differ
            for j in range(min_len):
                if word1[j] != word2[j]:
                    adjacency[word1[j]].append(word2[j])
                    in_degree[word2[j]] += 1
                    break

        # for src in adjacency:
        #     for dest in adjacency[src]:
        #         in_degree[dest] += 1

        queue = deque([char for char in in_degree if in_degree[char] == 0])
        
        order = []

        while queue:
            char = queue.popleft()
            order.append(char)

            for nei in adjacency[char]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)

        print(order)

        if len(order) == len(in_degree):
            return ''.join(order)
        else:
            return ''

                

        