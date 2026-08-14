class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)

        if n == 1:
            return 1

        l1 = [0] * (n - 1)
        l2 = [0] * (n - 1)

        for i in range(n - 1):
            if i % 2 == 1:
                l1[i] = arr[i] > arr[i + 1]
                l2[i] = arr[i] < arr[i + 1]
            else:
                l1[i] = arr[i] < arr[i + 1]
                l2[i] = arr[i] > arr[i + 1]

        
        maxLen = 0

        l = 0
        for r in range(n - 1):
            if l1[r]:
                maxLen = max(maxLen, r - l + 1)
            else:
                l = r + 1

        l = 0
        for r in range(n - 1):
            if l2[r]:
                maxLen = max(maxLen, r - l + 1)
            else:
                l = r + 1

        return maxLen + 1


        