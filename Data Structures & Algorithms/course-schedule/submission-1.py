class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        visited = set()

        def dfs(course):

            if course in visited:
                return False

            if preMap[course] == []:
                return True

            visited.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            preMap[course] = [] # ie removing course's prerequisites
            return True

        for course in preMap:
            if not dfs(course):
                return False
        return True