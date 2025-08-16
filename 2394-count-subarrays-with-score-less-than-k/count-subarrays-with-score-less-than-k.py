from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        lp = 0
        window_sum = 0
        res = 0

        for rp, val in enumerate(nums):
            window_sum += val

            # shrink window while score too big
            while window_sum * (rp - lp + 1) >= k:
                window_sum -= nums[lp]
                lp += 1

            # all subarrays ending at rp and starting between lp..rp are valid
            res += rp - lp + 1

        return res
