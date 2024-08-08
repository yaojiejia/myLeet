from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        visited = set()
        total_cells = rows * cols
        direction_index = 0
        x, y = 0, 0
        res = []

        while len(visited) < total_cells:
            res.append(matrix[x][y])
            visited.add((x, y))
            new_x, new_y = x + directions[direction_index][0], y + directions[direction_index][1]

            if 0 <= new_x < rows and 0 <= new_y < cols and (new_x, new_y) not in visited:
                x, y = new_x, new_y
            else:
                direction_index = (direction_index + 1) % 4
                x += directions[direction_index][0]
                y += directions[direction_index][1]

        return res
