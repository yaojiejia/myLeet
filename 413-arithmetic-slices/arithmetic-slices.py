from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res = 0
        lp = 0

        if len(nums) < 3:
            return 0

        last_diff = nums[1] - nums[0]
        for rp in range(1, len(nums)):
            if nums[rp] - nums[rp-1] != last_diff:
                lp = rp - 1  # restart window at previous element
            last_diff = nums[rp] - nums[rp-1]

            if (rp - lp + 1) >= 3:
                res += (rp - lp + 1) - 2   # count all slices ending at rp

        return res
