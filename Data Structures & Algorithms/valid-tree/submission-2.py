class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adjacency = defaultdict(list)
        for a, b in edges:
            adjacency[a].append(b)
            adjacency[b].append(a)

        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)

            for nei in adjacency[i]:
                if nei == prev:
                    continue
                if not dfs(nei, i):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
