# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        
        root = preorder[0]
        tree = TreeNode(root)

        rootIndex = 0
        while inorder[rootIndex] != root:
            rootIndex += 1

        # rootIndex = find(inorder, root)
        left_inOrder = inorder[:rootIndex]
        right_inOrder = inorder[rootIndex+1:]

        left_preOrder = preorder[1:1+len(left_inOrder)]
        right_preOrder = preorder[1+len(left_inOrder):]

        tree.left = self.buildTree(left_preOrder, left_inOrder)
        tree.right = self.buildTree(right_preOrder, right_inOrder)
        
        return tree
