class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)

        # sort by descending position
        data = zip(position, speed)
        cars = sorted(data, key = lambda x: -x[0])

        fleets = 0
        last_time = 0

        for pos, speed in cars:
            time = (target - pos) / speed

            if time > last_time:
                fleets += 1
                last_time = time

        return fleets
