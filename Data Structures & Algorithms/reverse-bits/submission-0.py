class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0

        for i in range(32):
            # get i-th bit of n
            bit = (n >> i) & 1

            # put it into res
            res = res | (bit << (31 - i))

        return res