class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_cnt = 0
        lp = 0
        res = 0

        for rp in range(len(nums)):
            if nums[rp] == 0:
                zero_cnt += 1
            
            while zero_cnt > k:
                if nums[lp] == 0:
                    zero_cnt -= 1
                lp += 1
            res = max(res, rp-lp+1)
        return res