class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        n = len(people)

        people.sort()

        boats = 0

        l = 0
        r = n - 1

        while l <= r:
            if people[l] + people[r] <= limit:
                boats += 1
                l += 1
                r -= 1

            else:   # if we cant put both, we put fattest in its own boat, and keep trying to match smallest with 2nd fattest
                boats += 1
                r -= 1                

        return boats