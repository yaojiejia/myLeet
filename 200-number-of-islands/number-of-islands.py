from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        res = 0

        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for xDir, yDir in directions:
                    newR, newC = row + xDir, col + yDir
                    if (newR in range(rows) and newC in range(cols) and (newR, newC) not in visit and grid[newR][newC] == "1"):
                        q.append((newR, newC))
                        visit.add((newR, newC))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    res += 1
                    bfs(r, c)

        return res
