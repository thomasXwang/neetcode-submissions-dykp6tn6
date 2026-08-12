class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        
        great = float('-inf')
        prev = arr[n - 1]

        i = n - 1

        while i >= 0:
            great = max(prev, great)
            prev = arr[i - 1]
            arr[i - 1] = great

            i -= 1

        arr[n - 1] = -1

        return arr