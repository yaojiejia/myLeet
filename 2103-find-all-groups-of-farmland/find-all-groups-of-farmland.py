from collections import deque
from typing import List

class Solution:
    def findFarmland(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    coord = [r,c,-1,-1]
                    maxRow,maxCol = r,c
                    grid[r][c] = 0
                    q = deque([(r, c)])
                    while q:
                        row, col = q.popleft()
                        for dx, dy in direction:
                            newRow = row + dx
                            newCol = col + dy
                            if 0 <= newRow < rows and 0 <= newCol < cols and grid[newRow][newCol] == 1:
                                grid[newRow][newCol] = 0
                                maxRow = max(maxRow,newRow)
                                maxCol = max(maxCol,newCol)
                                q.append((newRow, newCol))
                    coord[2],coord[3] = maxRow, maxCol
                    res.append(coord)
                            
        return res