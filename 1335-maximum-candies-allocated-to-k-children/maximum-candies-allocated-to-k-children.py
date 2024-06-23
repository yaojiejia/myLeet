class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        lp = 1
        rp = max(candies)
        
        while lp <= rp:
            mid = lp+(rp-lp)//2
            pile = 0
            for c in candies:
                pile += c//mid
            if pile >= k:
                
                lp = mid + 1
            else:
                rp = mid -1
        return rp
        