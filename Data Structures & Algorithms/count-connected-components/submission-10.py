class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # visited tracker
        visited = [False] * n

        def bfs(node):
            q = deque([node])
            while q:
                nod = q.popleft()
                visited[nod] = True
                for nei in graph[nod]:
                    if not visited[nei]:
                        q.append(nei)

        components = 0
        for node in range(n):
            if not visited[node]:
                components += 1
                visited[node] = True
                bfs(node)
        return components