class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0xffffffff
        max_int = 0x7fffffff

        if not b and not a:
            return 0
        
        # put b as non-null
        if not b:
            a, b = b, a
        
        sum_ = a
        carry = b

        while carry:
            new_sum_ = (sum_ ^ carry) & mask
            carry = ((sum_ & carry) << 1 ) & mask
            sum_ = new_sum_

        return sum_ if sum_ <= max_int else ~(sum_ ^ mask)