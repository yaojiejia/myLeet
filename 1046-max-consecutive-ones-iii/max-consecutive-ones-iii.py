class Solution(object):
    def longestOnes(self, nums, k):
        count = 0
        res = 0
        lp = 0
        length = len(nums)
        for rp in range(length):
            if nums[rp] == 1:
                count += 1

            while (rp - lp + 1) - count > k:
                if nums[lp] == 1:
                    count -= 1
                lp += 1
            
            res = max(res, rp - lp + 1)
        return res
