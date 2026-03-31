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

        i = 0
        prev = -1
        while len(visited) != n:
            if i not in visited:
                dfs(i, prev)
                count += 1
            i += 1


        return count

            
            