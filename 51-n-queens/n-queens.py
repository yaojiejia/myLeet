class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDia = set()
        negDia = set()

        board = [["."] * n for _ in range(n)]
        res = []

        def f(r):
            if r == n:
                c = ["".join(row) for row in board]
                res.append(c)
                return
            
            for c in range(n):
                if c in col or (r+c) in posDia or (r-c) in negDia:
                    continue
                
                col.add(c)
                posDia.add(r+c)
                negDia.add(r-c)
                board[r][c] = "Q"
                f(r+1)
                col.remove(c)
                posDia.remove(r+c)
                negDia.remove(r-c)
                board[r][c] = "."
        f(0)
        return res



