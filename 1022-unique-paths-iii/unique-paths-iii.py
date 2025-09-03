class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        start = None
        end = None
        empty = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    start = [r,c]
                if grid[r][c] == 2:
                    end = [r,c]
                if grid[r][c] != -1:
                    empty += 1
        result = 0

        def dfs(r,c,empty_cnt):
            nonlocal result
            if not (0 <= r < row and 0 <= c < col) or grid[r][c] == -1:
                return 
            if [r,c] == end and empty_cnt == empty:
                result += 1 
                return
            
            temp = grid[r][c]
            grid[r][c] = -1
            dfs(r+1, c, empty_cnt + 1)
            dfs(r-1, c, empty_cnt + 1)
            dfs(r, c+1, empty_cnt + 1)
            dfs(r, c-1, empty_cnt + 1)
            grid[r][c] = temp
        
        dfs(start[0], start[1], 1)
        return result

        
