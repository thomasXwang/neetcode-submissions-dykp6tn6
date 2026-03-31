# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, currentMax):

            # base case
            if not node:
                return 0
            
            if node.val >= currentMax:
                count = 1
                newMax = node.val
            else:
                count = 0
                newMax = currentMax

            count += dfs(node.left, newMax)
            count += dfs(node.right, newMax)

            return count

        return dfs(root, root.val)
