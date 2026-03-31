class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        a, b, c = target

        currMax = [0] * 3

        for i, j, k in triplets:
            if i > a or j > b or k > c:
                continue
            currMax[0] = max(currMax[0], i)
            currMax[1] = max(currMax[1], j)
            currMax[2] = max(currMax[2], k)

            if currMax == target:
                return True
        
        return False