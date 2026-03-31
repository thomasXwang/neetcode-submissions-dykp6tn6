class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for src, tar, time in times:
            graph[src].append((time, tar))

        minHeap = [(0, k)]
        visited = set()

        time = 0

        while minHeap:
            t, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            time = t

            for t_nei, nei in graph[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (t + t_nei, nei))

        if len(visited) == n:
            return time
        return -1
