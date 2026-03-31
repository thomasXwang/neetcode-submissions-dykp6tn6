class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)

        l = 0
        r = 0

        res = []
        q = collections.deque()

        while r < n:
            # remove out of bounds left indices
            if q and q[0] < l:
                q.popleft()

            # prepare the deque so that decreasing property is maintained after we add the current index
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if r >= k - 1:
                res.append(nums[q[0]])
                l += 1

            r += 1

        return res