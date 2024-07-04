class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for city1, city2 in connections:
            graph[city1].append((city2,1))
            graph[city2].append((city1,0))
        def dfs(node, parent):
            change_count = 0
            for neighbor, direction in graph[node]:
                if neighbor != parent:
                    change_count += direction
                    change_count += dfs(neighbor, node)
            return change_count

        return dfs(0, -1)