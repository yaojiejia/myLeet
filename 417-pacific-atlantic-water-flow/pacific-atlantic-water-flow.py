class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        p = set()
        a = set()

        def dfs(r,c,visit,prevHeight):
            if ((r,c) in visit or r < 0 or c < 0 or r >= rows or c >= cols or heights[r][c] < prevHeight):
                return 
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])



        for c in range(cols):
            dfs(0, c, p, heights[0][c])
            dfs(rows-1, c, a, heights[rows-1][c])
        for r in range(rows):
            dfs(r, 0, p, heights[r][0])
            dfs(r, cols-1, a, heights[r][c])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in p and (r,c) in a:
                    res.append([r,c])
        return res