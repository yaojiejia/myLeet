
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the adjacency list
        adj_list = {i: [] for i in range(numCourses)}
        for u, v in prerequisites:
            adj_list[v].append(u)
        
        visited = set()
        visited_global = set()
        
        def dfs(node):
            if node in visited:
                return False
            if node in visited_global:
                return True
            
            visited.add(node)
            for neighbor in adj_list[node]:
                if not dfs(neighbor):
                    return False
            visited.remove(node)
            visited_global.add(node)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True