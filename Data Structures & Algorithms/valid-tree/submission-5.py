class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adjacency = defaultdict(list)
        for a, b in edges:
            adjacency[a].append(b)
            adjacency[b].append(a)

        visited = set()

        # indicates if the connected component of node is acyclic
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)

            for nei in adjacency[node]:
                if nei == parent:
                    continue
                if dfs(nei, node) == False:
                    return False
            return True
                
        

        return dfs(0, -1) and len(visited) == n