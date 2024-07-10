from collections import deque
from typing import List, Optional

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        
        # Initialize the queue with the position of all rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        # If there are no rotten oranges at the start, return -1
        if not queue:
            if any(1 in row for row in grid):
                return -1
            else:
                return 0
        
        # BFS to rot the fresh oranges
        minutes_passed = -1
        
        while queue:
            minutes_passed += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
        
        # If there are still fresh oranges left, return -1
        if any(1 in row for row in grid):
            return -1
        
        return minutes_passed

