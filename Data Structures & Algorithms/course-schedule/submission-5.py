class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1

        q = deque([c for c in range(numCourses) if in_degree[c] == 0])

        count = 0

        while q:
            course = q.popleft()

            for seq in graph[course]:
                in_degree[seq] -= 1
                if in_degree[seq] == 0:
                    q.append(seq)
            count += 1

        return count == numCourses

