class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # monotonic decreasing stack
        res = []
        s = []
        for i in range(len(heights)-1, -1, -1):
        
            while s and heights[i] > s[-1]:
                s.pop()
            s.append(heights[i])
            if len(s) == 1:
                res.append(i)
        return sorted(res)