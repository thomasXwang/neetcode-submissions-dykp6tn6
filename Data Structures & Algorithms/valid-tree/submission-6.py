class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                if dfs(nei, node) == False:
                    return False
            return True

        return dfs(0, -1) and len(visited) == n