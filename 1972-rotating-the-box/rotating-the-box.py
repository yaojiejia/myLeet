class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        rotated = [["_"] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated[j][m - 1 - i] = boxGrid[i][j]

        for c in range(m):
            empty = n - 1
            for r in range(n - 1, -1, -1):
                if rotated[r][c] == "*":
                    empty = r - 1
                elif rotated[r][c] == "#":
                    rotated[r][c] = "."
                    rotated[empty][c] = "#"
                    empty -= 1
        return rotated