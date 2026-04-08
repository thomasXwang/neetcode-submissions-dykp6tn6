class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []

        for name in path.split('/'):
            if name == '' or name == '.':
                continue
            elif name == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(name)

        # print(stack)
        
        return '/' + '/'.join(stack)
