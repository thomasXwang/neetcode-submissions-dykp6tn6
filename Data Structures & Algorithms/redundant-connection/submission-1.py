class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)

        par = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(node):
            while node != par[node]:
                par[node] = par[par[node]]
                node = par[node]
            return node

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return False

            if rank[p1] < rank[p2]:
                rank[p2] += rank[p1]
                par[p1] = p2
            else:
                rank[p1] += rank[p2]
                par[p2] = p1

            return True

        for a, b in edges:
            if union(a, b) == False:
                return [a, b]