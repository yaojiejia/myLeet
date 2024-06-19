from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        rows, cols = len(board), len(board[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def capture(r, c):
            board[r][c] = "T"
            q = deque([(r, c)])
            while q:
                row, col = q.popleft()
                for dx, dy in direction:
                    newR, newC = row + dx, col + dy
                    if 0 <= newR < rows and 0 <= newC < cols and board[newR][newC] == "O":
                        board[newR][newC] = "T"
                        q.append((newR, newC))

        # Capture unsurrounded regions (connected to edges)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows-1] or c in [0, cols-1]):
                    capture(r, c)

        # Flip all remaining 'O' to 'X'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # Flip all 'T' back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"

        return board
