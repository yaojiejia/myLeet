class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in row] for row in grid]
        dp[0][0] = grid[0][0]

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue
                top = dp[r-1][c] if r-1 >= 0 else float('inf')
                left = dp[r][c-1] if c-1 >= 0 else float('inf')
                dp[r][c] = grid[r][c] + min(top, left)

        return dp[rows-1][cols-1]
