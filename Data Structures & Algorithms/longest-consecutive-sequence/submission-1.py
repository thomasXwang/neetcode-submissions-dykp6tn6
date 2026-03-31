class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        longest = 0
        subsequences = []

        for i, element in enumerate(nums):
            if (element-1) in numSet:
                pass
            else:
                subsequence = [element]
                next_ele = element+1
                while next_ele in numSet:
                    subsequence.append(next_ele)
                    next_ele += 1
                subsequences.append(subsequence)

        for subsequence in subsequences:
            if len(subsequence) > longest:
                print(subsequence)
                longest = len(subsequence)

        return longest

        