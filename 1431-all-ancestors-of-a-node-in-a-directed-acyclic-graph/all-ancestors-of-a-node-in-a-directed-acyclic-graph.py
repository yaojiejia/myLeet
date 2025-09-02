from collections import defaultdict, deque
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj_list = defaultdict(list)
        indeg = defaultdict(int)
        
        for u, v in edges:
            adj_list[u].append(v)
            indeg[v] += 1
        for u, v in edges:
            if u not in indeg:
                indeg[u] = 0

        q = deque()
        ans = {i: set() for i in range(n)}  # initialize empty sets

        for key, value in indeg.items():
            if value == 0:
                q.append(key)
                    
        while q:
            node = q.popleft()
            
            for child in adj_list[node]:
                # update child’s ancestor set
                ans[child].update(ans[node])  # inherit all ancestors from parent
                ans[child].add(node)          # add parent itself
                
                indeg[child] -= 1
                if indeg[child] == 0:
                    q.append(child)
        
        # convert sets to sorted lists
        return [sorted(list(ans[i])) for i in range(n)]
