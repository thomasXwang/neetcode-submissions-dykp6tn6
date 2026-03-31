class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        a, b, c = target

        max1 = max2 = max3 = 0

        for i, j, k in triplets:
            if i > a or j > b or k > c:
                continue
            max1 = max(max1, i)
            max2 = max(max2, j)
            max3 = max(max3, k)
        
        return [max1, max2, max3] == target