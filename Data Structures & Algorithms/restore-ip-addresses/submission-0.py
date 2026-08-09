class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        n = len(s)
        
        res = []

        curr = []

        def dfs(i, parts):
            if i == n:
                if parts == 4:
                    res.append('.'.join(curr))
                return
            
            if i > n:
                return

            for length in range(1, 4):
                if i + length > n:
                    return

                part = s[i: i + length]
                
                if len(part) > 1 and part[0] == '0':
                    break

                if int(part) > 255:
                    continue 

                curr.append(part)
                dfs(i + length, parts + 1)
                curr.pop()


        dfs(0, 0)

        return res