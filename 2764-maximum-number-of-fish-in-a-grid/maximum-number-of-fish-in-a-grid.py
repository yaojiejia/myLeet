class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    temp = grid[r][c]
                    grid[r][c] = 0
                    q = deque([(r,c)])

                    while q:
                        row, col = q.popleft()
                        for dx,dy in direction:
                            newR = row+dx
                            newC = col+dy
                            if 0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] != 0:
                                temp += grid[newR][newC]
                                grid[newR][newC] = 0
                                q.append((newR,newC))
                    res = max(res,temp)
        return res