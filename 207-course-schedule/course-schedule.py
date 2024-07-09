
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the adjacency list
        adj_list = {i: [] for i in range(numCourses)}
        for u, v in prerequisites:
            adj_list[v].append(u)
        
        visited = set()
        
        def dfs(node):
            if node in visited:
                return False
            if adj_list == []:
                return True

            
            visited.add(node)
            for neighbor in adj_list[node]:
                if not dfs(neighbor):
                    return False
            visited.remove(node)
            adj_list[node] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True