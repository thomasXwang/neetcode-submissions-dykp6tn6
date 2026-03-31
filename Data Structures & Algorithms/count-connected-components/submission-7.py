class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        par = list(range(n))
        ranks = [1] * n

        def find(node):
            res = node
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return 0

            if ranks[p1] > ranks[p2]:
                par[p2] = p1
                ranks[p1] += ranks[p2]
            else:
                par[p1] = p2
                ranks[p2] += ranks[p1]

            return 1

        res = n
        for a, b in edges:
            if union(a, b):
                res -= 1

        return res
