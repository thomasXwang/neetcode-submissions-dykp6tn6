class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        q = collections.deque([(0, -1)])

        while q:
            node, parent = q.popleft()
            visited.add(node)

            for nei in graph[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                visited.add(node)
                q.append((nei, node))

        return len(visited) == n