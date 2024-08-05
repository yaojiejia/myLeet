from typing import List
from collections import deque, defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def bfs(path, start):
            q = deque([(start, 0)])
            visited = {}
            
            while q:
                curr, curr_dist = q.popleft()
                if curr not in visited or curr_dist < visited[curr]:
                    visited[curr] = curr_dist
                    for neighbor, time in path[curr]:
                        q.append((neighbor, curr_dist + time))
            
            if len(visited) == n:
                return max(visited.values())
            return -1

        adj_list = defaultdict(list)
        for u, v, t in times:
            adj_list[u].append((v, t))
        
        return bfs(adj_list, k)
