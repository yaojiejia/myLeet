from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        res = 0
        lp = 0
        window = 1

        for rp, num in enumerate(nums):
            window *= num
            while window >= k and lp <= rp:
                window //= nums[lp]
                lp += 1
            res += rp - lp + 1   # count all subarrays ending at rp

        return res
