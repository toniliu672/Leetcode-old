class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        times = [[float('inf')] * 2 for _ in range(n + 1)]
        times[1][0] = 0
        queue = [(0, 1)]
        
        while queue:
            curr_time, node = heapq.heappop(queue)
            
            for neighbor in graph[node]:
                wait = 0
                if (curr_time // change) % 2:
                    wait = change - (curr_time % change)
                
                next_time = curr_time + wait + time
                
                if next_time < times[neighbor][0]:
                    times[neighbor][0] = next_time
                    heapq.heappush(queue, (next_time, neighbor))
                elif times[neighbor][0] < next_time < times[neighbor][1]:
                    times[neighbor][1] = next_time
                    heapq.heappush(queue, (next_time, neighbor))
                
                if times[n][1] != float('inf'):
                    return times[n][1]
        
        return -1