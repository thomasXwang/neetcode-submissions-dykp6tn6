# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None:
            new_tree = root
        else:
            # Recursively invert the left and right subtrees
            new_left = self.invertTree(root.right)
            new_right = self.invertTree(root.left)

            # Create a new tree with swapped left and right children
            new_tree = TreeNode(root.val, new_left, new_right)
        
        return new_tree