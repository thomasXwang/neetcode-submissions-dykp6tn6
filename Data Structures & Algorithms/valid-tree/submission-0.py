class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if n == 0:
            return True
        
        adjacency = defaultdict(list)
        for a, b in edges:
            adjacency[a].append(b)
            adjacency[b].append(a)

        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(i)
            for nei in adjacency[i]:
                if nei == prev:
                    continue
                if not dfs(nei, i):
                    return False
            return True

        

        return dfs(0, -1) and len(visit) == n