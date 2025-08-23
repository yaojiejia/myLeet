from collections import deque
from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        island_id = 2   # start ids from 2 (since 0,1 already used)
        island_size = {}  # id -> size

        # Preprocess: label islands with ID and record their size
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    q = deque([(r, c)])
                    grid[r][c] = island_id
                    size = 0
                    while q:
                        row, col = q.popleft()
                        size += 1
                        for dx, dy in directions:
                            nr, nc = row + dx, col + dy
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                                grid[nr][nc] = island_id
                                q.append((nr, nc))
                    island_size[island_id] = size
                    island_id += 1

        res = max(island_size.values() or [0])  # handle case with no 1's

        # Try flipping each 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    seen_ids = set()
                    curr_res = 1  # flip this cell
                    for dx, dy in directions:
                        nr, nc = r + dx, c + dy
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 1:
                            seen_ids.add(grid[nr][nc])
                    for id_ in seen_ids:
                        curr_res += island_size[id_]
                    res = max(res, curr_res)

        return res
