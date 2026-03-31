class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1

        q = deque([node for node in range(numCourses) if in_degree[node] == 0])

        count = 0

        while q:
            course = q.popleft()

            for dest in graph[course]:
                in_degree[dest] -= 1
                if in_degree[dest] == 0:
                    q.append(dest)

            count += 1
        
        if count == numCourses:
            return True
        return False

            
            