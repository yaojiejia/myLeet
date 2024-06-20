from collections import deque
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows = len(grid1)
        cols = len(grid1[0])
        res = 0
      

        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=cols or grid2[i][j]==0:
                return
            
            grid2[i][j]=0
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i-1,j)
        
        for r in range(rows):
            for c in range(cols):
                if grid1[r][c] == 0 and grid2[r][c] == 1:
                    dfs(r,c)
                    

        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1:
                    res += 1
                    dfs(r,c)
        return res
                