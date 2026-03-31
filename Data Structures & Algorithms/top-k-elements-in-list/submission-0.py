class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        # building a hashmap of counts
        for n in nums:
            count[n] += 1
        
        for n, count in count.items():
            freq[count].append(n)

        res = []

        for i in range(len(freq)-1, 0, -1):

            print(i)
            print(freq[i])

            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        return res

        
        