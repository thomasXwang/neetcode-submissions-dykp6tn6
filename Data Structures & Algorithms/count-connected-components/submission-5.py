class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjacency = defaultdict(list)
        for a, b in edges:
            adjacency[a].append(b)
            adjacency[b].append(a)

        visited = set()

        count = 0

        def bfs(node):
            q = deque([node])
            visited.add(node)

            while q:
                node = q.popleft()
                for nei in adjacency[node]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)

        for i in range(n):
            if i not in visited:
                bfs(i)
                count += 1
        return count
