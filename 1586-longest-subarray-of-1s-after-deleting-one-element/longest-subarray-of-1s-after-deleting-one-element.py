class Solution(object):
    def longestSubarray(self, nums):
        k = 1
        count = 0
        res = 0
        lp = 0
        for rp in range(len(nums)):
            if nums[rp] == 1:
                count += 1
            
            while (rp-lp + 1) - count > k:
                if nums[lp] == 1:
                    count -= 1
                lp += 1
            res = max(res, (rp-lp+1))
        return res - 1
        

        