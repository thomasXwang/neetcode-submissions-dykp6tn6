"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        oldToNew = {}
        
        def dfs(node):

            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy

            for neighbor in node.neighbors:
                neighbor_copy = dfs(neighbor)
                # copy.neighbors.append(neighbor_copy)
                neighbor_copy.neighbors.append(copy )

            return copy

        return dfs(node) if node else None


        