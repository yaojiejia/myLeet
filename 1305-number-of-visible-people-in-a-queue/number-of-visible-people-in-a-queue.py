class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        s = []
        res = []
        # monotonic decreasing bc going from right to left
        # if curr is taller than the last, then none of the people in front of curr can see the last
        #  1 1 0
        # if blocked then curr max gets updated
        # how do we find blocked? if curr is less than last
        # [11,8]
        
        for i in range(len(heights)-1, -1, -1):

            ppl = 0
            while s and heights[i] > s[-1]:
                ppl += 1
                s.pop()
            
            if s:
                ppl += 1
            res.append(ppl)
            s.append(heights[i])

        return res[::-1]