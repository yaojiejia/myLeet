class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        lp = 1
        rp = max(candies)
        res = 0
        while lp <= rp:
            mid = lp+(rp-lp)//2
            pile = 0
            for c in candies:
                pile += math.floor(c/mid)
            if pile >= k:
                res = max(res,mid)
                lp = mid + 1
            else:
                rp = mid -1
        return res
        