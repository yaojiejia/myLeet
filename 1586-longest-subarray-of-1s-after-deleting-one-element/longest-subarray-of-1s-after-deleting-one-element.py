class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        lp = 0

        zero_cnt = 0
        for rp in range(len(nums)):
            if nums[rp] == 0:
                zero_cnt += 1
            while zero_cnt > 1:
                if nums[lp] == 0:
                    zero_cnt -= 1
                lp += 1
            res = max(res, rp-lp+1)
        return res-1