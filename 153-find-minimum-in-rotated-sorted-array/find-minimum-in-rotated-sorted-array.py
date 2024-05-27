class Solution(object):
    def findMin(self, nums):
        lp = 0
        rp = len(nums)-1
        res = nums[0]
        while lp <= rp:
            if nums[lp] < nums[rp]:
                return min(res, nums[lp])
            mid = (lp + rp) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[lp]:
                lp = mid + 1
            else:
                rp = mid - 1
        return res