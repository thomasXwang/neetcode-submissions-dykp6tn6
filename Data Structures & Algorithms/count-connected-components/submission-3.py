class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjacency = defaultdict(list)
        for a, b in edges:
            adjacency[a].append(b)
            adjacency[b].append(a)

        visited = set()

        count = 0

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for nei in adjacency[node]:
                dfs(nei)

        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count