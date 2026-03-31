class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A, B = nums1, nums2
        # put A as the shortest length array
        if len(A) > len(B):
            A, B = B, A

        m = len(A)
        n = len(B)

        half = (m + n) // 2

        # Binary search on the shortest array A
        l = 0
        r = m - 1

        while True:
            # find mid
            i = (l + r) // 2
            # find leftover that allows to get a total half array
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if i + 1 < m else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if j + 1 < n else float('inf')

            print(i, j)
            print(Aleft, Aright, Bleft, Bright)

            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if (m + n) % 2:
                    print(Aright, Bright)
                    return min(Aright, Bright)
                # even
                else:
                    return ( max(Aleft, Bleft) + min(Aright, Bright) ) / 2
            elif Bleft > Aright:
                l = i + 1
            elif Aleft > Bright:
                r = i - 1
