class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)

        total = sum(matchsticks)

        if total % 4 != 0:
            return False
        
        target = total // 4

        matchsticks.sort(reverse=True)
        if matchsticks[0] > target:
            return False
        
        res = False

        def dfs(i, sides):
            if i == n:
                return sides[0] == sides[1] == sides[2] == sides[3]
            
            stick = matchsticks[i]

            for j in range(4):
                if stick + sides[j] <= target:
                    new_sides = list(sides)
                    new_sides[j] += stick
                    
                    if dfs(i + 1, sorted(tuple(new_sides))):
                        return True

            return False


        return dfs(0, (0, 0, 0, 0))

