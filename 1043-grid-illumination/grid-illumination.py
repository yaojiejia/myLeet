from collections import Counter
from typing import List

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
        row = Counter()
        col = Counter()
        posDia = Counter()
        negDia = Counter()
        lampSet = set()

        # initialize lamp counts
        for r, c in lamps:
            if (r, c) in lampSet:
                continue
            lampSet.add((r, c))
            row[r] += 1
            col[c] += 1
            posDia[r+c] += 1
            negDia[r-c] += 1

        res = []
        for r, c in queries:
            # check illumination
            if row[r] > 0 or col[c] > 0 or posDia[r+c] > 0 or negDia[r-c] > 0:
                res.append(1)
            else:
                res.append(0)

            # turn off (r, c) first if lamp exists
            if (r, c) in lampSet:
                lampSet.remove((r, c))
                row[r] -= 1
                col[c] -= 1
                posDia[r+c] -= 1
                negDia[r-c] -= 1

            # then turn off neighbors
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if (nr, nc) in lampSet:
                    lampSet.remove((nr, nc))
                    row[nr] -= 1
                    col[nc] -= 1
                    posDia[nr+nc] -= 1
                    negDia[nr-nc] -= 1

        return res
