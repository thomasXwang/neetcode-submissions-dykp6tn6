class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)

        cand1 = cand2 = None
        count1 = count2 = 0

        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

            # print(cand1, count1)
            # print(cand2, count2)
        
        count1 = count2 = 0
        
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1

        # print()
        
        res = []
        if count1 > n // 3:
            res.append(cand1)
        if count2 > n // 3:
            res.append(cand2)
        return res
            