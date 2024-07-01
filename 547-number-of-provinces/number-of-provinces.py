class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            visited.add(i)
            for j in range(n):
                if j not in visited and isConnected[i][j] == 1:
                    dfs(j)

        n = len(isConnected)
        visited = set()
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1

        return res
