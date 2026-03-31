class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        par = [i for i in range(n)]
        rank = [1] * n

        # find root parent (ie representative) of node n
        def find(n1):
            res = n1

            while res != par[res]:
                # path compression
                par[res] = find(par[res])
                res = par[res]
            return res

        # create an edge between root parents of nodes n1 & n2
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            # if same parents, return 0 to signify we didn't perform union
            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        components = n
        for n1, n2 in edges:
            components -= union(n1, n2)
        return components