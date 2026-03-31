class Solution:
    def isHappy(self, n: int) -> bool:

        digits = [int(d) for d in str(n)]
        
        squareSum = 0
        prev = set()

        while squareSum != 1:
            digits = [int(d) for d in str(n)]
            squareSum = sum([i**2 for i in digits])
            if squareSum in prev:
                return False
            prev.add(squareSum)
            n = squareSum
        return True
