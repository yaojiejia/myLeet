from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0
        maze[entrance[0]][entrance[1]] = '+' 
        q = deque([entrance])
        while q:
            res += 1  
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    newX, newY = x + dx, y + dy
                    if 0 <= newX < rows and 0 <= newY < cols and maze[newX][newY] == '.':
                        if newX in {0, rows - 1} or newY in {0, cols - 1}: 
                            return res
                        maze[newX][newY] = '+'
                        q.append((newX, newY))
                
        return -1

                

