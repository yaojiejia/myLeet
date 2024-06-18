from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        res = 0
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    res += 1
                    grid[r][c] = "0"
                    q = deque([(r, c)])
                    
                    while q:
                        row, col = q.popleft()
                        for dx, dy in direction:
                            newRow = row + dx
                            newCol = col + dy
                            if 0 <= newRow < rows and 0 <= newCol < cols and grid[newRow][newCol] == "1":
                                grid[newRow][newCol] = "0"
                                q.append((newRow, newCol))
        return res
