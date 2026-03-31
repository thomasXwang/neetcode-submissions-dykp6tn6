class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        counts = Counter(nums)

        for num, count in counts.items():
            if count >= n // 2:
                return num