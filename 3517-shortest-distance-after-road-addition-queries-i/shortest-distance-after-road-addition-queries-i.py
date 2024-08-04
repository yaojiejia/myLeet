from collections import deque, defaultdict
from typing import List

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def bfs(path, start, end):
            q = deque([(start, 0)])  # Queue holds tuples of (node, distance)
            visited = set()
            
            while q:
                curr, curr_dist = q.popleft()

                if curr == end:
                    return curr_dist
                
                if curr not in visited:
                    visited.add(curr)
                    for neighbor in path[curr]:
                        if neighbor not in visited:
                            q.append((neighbor, curr_dist + 1))
            
            return -1

        path = defaultdict(list)
        res = []
        
        # Initialize the graph with directed edges from 0 to n-1
        for i in range(n - 1):
            path[i].append(i + 1)
        
        for t, d in queries:
            path[t].append(d)  # Add directed edge from t to d
            res.append(bfs(path, 0, n - 1))
        
        return res