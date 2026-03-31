# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return [-1, -1]

            extendableDiameterL, nonExtendableDiameterL = dfs(root.left)
            extendableDiameterR, nonExtendableDiameterR = dfs(root.right)

            nonExtendableDiameter = max(
                2 + extendableDiameterL + extendableDiameterR,
                nonExtendableDiameterL,
                nonExtendableDiameterR,
            )
            extendableDiameter = max(
                1 + extendableDiameterL,
                1 + extendableDiameterR
            )

            return [extendableDiameter, nonExtendableDiameter]

        extendableDiameter, nonExtendableDiameter = dfs(root)
        return max(extendableDiameter, nonExtendableDiameter)
