from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        cnt = 0
        lp = 0
        res = 0
        n = len(nums)

        for rp, val in enumerate(nums):
            if val == max_num:
                cnt += 1

            while cnt >= k:
                # all subarrays [lp..rp], [lp+1..rp], ... that start at lp
                # will still have ≥k maxes if we fix rp; there are (n - rp) choices for the end
                res += n - rp
                if nums[lp] == max_num:
                    cnt -= 1
                lp += 1

        return res
