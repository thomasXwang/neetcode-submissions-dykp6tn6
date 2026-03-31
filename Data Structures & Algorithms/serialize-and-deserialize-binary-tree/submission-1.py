# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        return f'{root.val}[{self.serialize(root.left)}][{self.serialize(root.right)}]'
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        if not data:
            return None
        print(data.split('[')[0])
        try:
            root_val = int( data.split('[')[0] )
        except:
            root_val = None
            return TreeNode(root_val)
        # print(root_val)
        len_root = len(data.split('[')[0])

        tree = TreeNode(root_val)

        i = len_root
        stack = [data[i]]

        while len(stack) != 0:
            i += 1
            if data[i] == '[':
                stack.append('[')
            elif data[i] == ']':
                stack.pop()
        print(data[len_root: i+1])
        data_left = data[len_root: i+1]
        data_right = data[i+1:]

        print(f'data_left: {data_left}')
        print(f'data_right: {data_right}')

        data_left = data_left[1:-1]
        data_right = data_right[1:-1]

        print(f'data_left: {data_left}')
        print(f'data_right: {data_right}')
        tree.left = self.deserialize(data_left)
        tree.right = self.deserialize(data_right)

        return tree
        