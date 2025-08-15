from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        max_num_cnt = {max_num: 0}
        lp = 0
        res = 0

        for rp in range(len(nums)):
            if nums[rp] == max_num:
                max_num_cnt[max_num] += 1

            while max_num_cnt[max_num] >= k:
                if nums[lp] == max_num:
                    max_num_cnt[max_num] -= 1
                lp += 1

            res += lp  # all starts before lp are valid

        return res
