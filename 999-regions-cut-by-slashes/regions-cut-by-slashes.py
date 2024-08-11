class Solution:
    def regionsBySlashes(self, grid):
        grid_size = len(grid)
        # Create a 3x3 matrix for each cell in the original grid
        expanded_grid = [[0] * (grid_size * 3) for _ in range(grid_size * 3)]
        DIRECTIONS = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),]

        for i in range(grid_size):
            for j in range(grid_size):
                base_row = i * 3
                base_col = j * 3
                if grid[i][j] == "\\":
                    expanded_grid[base_row][base_col] = 1
                    expanded_grid[base_row + 1][base_col + 1] = 1
                    expanded_grid[base_row + 2][base_col + 2] = 1
                elif grid[i][j] == "/":
                    expanded_grid[base_row][base_col + 2] = 1
                    expanded_grid[base_row + 1][base_col + 1] = 1
                    expanded_grid[base_row + 2][base_col] = 1
        print(expanded_grid)

        res = 0
        for i in range(len(expanded_grid)):
            for j in range(len(expanded_grid)):
                if expanded_grid[i][j] == 0:
                    res += 1
                    q = deque([(i,j)])
                    expanded_grid[i][j] = 1
                    while q:
                        r, c = q.popleft()
                        for dx, dy in DIRECTIONS:
                            newRow, newCol = r+dx, c+dy
                            if 0 <= newRow < len(expanded_grid) and 0 <= newCol < len(expanded_grid) and expanded_grid[newRow][newCol] == 0:
                                expanded_grid[newRow][newCol] = 1
                                q.append((newRow, newCol))
        return res