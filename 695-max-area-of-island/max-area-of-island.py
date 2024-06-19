from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    curRes = 0
                    q = deque([(r, c)])
                    grid[r][c] = 0  # mark as visited
                    while q:
                        row, col = q.popleft()
                        curRes += 1
                        for dx, dy in directions:
                            newR, newC = row + dx, col + dy
                            if 0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] == 1:
                                grid[newR][newC] = 0  # mark as visited
                                q.append((newR, newC))
                    max_area = max(max_area, curRes)
        return max_area
