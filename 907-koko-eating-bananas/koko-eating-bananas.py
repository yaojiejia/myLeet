class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lp = 1
        rp = max(piles)
        res = rp
        while lp <= rp:
            mid = lp+ (rp-lp) //2
            hour = 0 
            for p in piles:
                hour += math.ceil(p/mid)
            if hour <= h:
                res = min(res,mid)
                rp = mid - 1
            else:
                lp = mid + 1
        return res
