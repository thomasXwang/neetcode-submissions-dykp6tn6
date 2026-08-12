class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        
        great = -1
        for i in range(n - 1, -1, -1):
            great, arr[i] = max(great, arr[i]), great

        return arr