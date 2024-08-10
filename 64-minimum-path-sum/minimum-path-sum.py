class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        new_grid = [[0 for _ in range(c)] for _ in range(r)]
        new_grid[0][0] = grid[0][0]
        for i in range(1, c):
            new_grid[0][i] = new_grid[0][i-1] + grid[0][i] 

        for i in range(1, r):
            new_grid[i][0] = new_grid[i-1][0] + grid[i][0]
        
        for i in range(1, r):
            for j in range(1, c):
                new_grid[i][j] = min(grid[i][j]+new_grid[i-1][j],grid[i][j]+new_grid[i][j-1] )
        return new_grid[r-1][c-1]