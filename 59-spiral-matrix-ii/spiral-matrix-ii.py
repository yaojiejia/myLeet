class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        rows, cols = n, n
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        visited = set()
        total_cells = rows * cols
        direction_index = 0
        x, y = 0, 0
        cur_value = 1

        while len(visited) < total_cells:
            matrix[x][y] = cur_value
            visited.add((x, y))
            new_x, new_y = x + directions[direction_index][0], y + directions[direction_index][1]

            if 0 <= new_x < rows and 0 <= new_y < cols and (new_x, new_y) not in visited:
                x, y = new_x, new_y
            else:
                direction_index = (direction_index + 1) % 4
                x += directions[direction_index][0]
                y += directions[direction_index][1]
            cur_value += 1
        return matrix


