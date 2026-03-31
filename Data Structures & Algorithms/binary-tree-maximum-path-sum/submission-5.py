# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # res = [root.val]

        # return max path sum without splitting
        def dfs(root):
            if not root:
                return 0, float('-inf')

            leftMax, leftMaxNoRoot = dfs(root.left)
            rightMax, rightMaxNoRoot = dfs(root.right)

            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            extendableMax = root.val + max(leftMax, rightMax)
            nonExtendableMax = max(leftMaxNoRoot, rightMaxNoRoot, root.val + leftMax + rightMax)

            return extendableMax, nonExtendableMax

        extendableMax, nonExtendableMax = dfs(root)

        return nonExtendableMax
        # return max(extendableMax, nonExtendableMax)
        