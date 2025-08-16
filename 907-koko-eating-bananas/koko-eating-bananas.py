from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lp = 1                      # min possible speed
        rp = max(piles)             # max possible speed
        res = rp

        while lp <= rp:
            mid = (lp + rp) // 2    # candidate speed

            # hours needed at this speed
            total_hours = sum(math.ceil(p / mid) for p in piles)

            if total_hours <= h:    # can finish in time, try smaller speed
                res = mid
                rp = mid - 1
            else:                   # need to eat faster
                lp = mid + 1

        return res
