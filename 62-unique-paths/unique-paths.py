class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for _ in range(m-1):
            curr = [1]*n
            for j in range(1, n):
                curr[j] = curr[j-1] + row[j]
            row = curr
        return row[-1]
