class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1

        k = m + n - 1

        while i >= 0 or j >= 0:
            a = nums1[i] if i >= 0 else float('-inf')
            b = nums2[j] if j >= 0 else float('-inf')
        
            if a > b:
                nums1[k] = a
                i -= 1
            else:
                nums1[k] = b
                j -= 1
            
            k -= 1