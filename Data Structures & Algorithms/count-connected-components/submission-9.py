class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # visited tracker
        visited = [False] * n

        def dfs(node):
            visited[node] = True
            for nei in graph[node]:
                if not visited[nei]:
                    # visited[nei] = True
                    dfs(nei)

        # count connected components
        components = 0
        for node in range(n):
            if not visited[node]:
                components += 1
                visited[node] = True
                dfs(node)

        return components