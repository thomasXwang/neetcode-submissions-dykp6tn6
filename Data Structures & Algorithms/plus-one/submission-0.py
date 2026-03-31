class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        res = []
        carry = 0
        add = 1
        
        for digit in reversed(digits):
            newDigit = (digit + carry + add) % 10
            carry = (digit + carry + add) // 10
            add = 0
            res.append(newDigit)
        
        if carry == 1:
            res.append(1)

        return res[::-1]