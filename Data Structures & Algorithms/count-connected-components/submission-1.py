class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjacency = defaultdict(list)
        for a, b in edges:
            adjacency[a].append(b)
            adjacency[b].append(a)

        visited = set()

        count = 0

        def dfs(i, prev):
            if i in visited:
                return 
            
            visited.add(i)

            for nei in adjacency[i]:
                if nei == prev:
                    continue
                dfs(nei, i)

        nodes = list(range(n))

        prev = -1
        for i in range(n):
            if i not in visited:
                dfs(i, prev)
                count += 1

        return count
            