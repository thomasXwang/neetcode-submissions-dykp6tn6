class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        in_nodes = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            in_nodes[course] += 1

        q = collections.deque([i for i in range(numCourses) if in_nodes[i] == 0])

        res = []

        while q:
            course = q.popleft()
            res.append(course)

            for nei in graph[course]:
                in_nodes[nei] -= 1
                if in_nodes[nei] == 0:
                    q.append(nei)
        
        if len(res) < numCourses:
            return []
        return res

