class Solution(object):
    def findMin(self, nums):
        lp = 0
        rp = len(nums)-1
        while lp < rp:
            mid = lp+(rp-lp) // 2
            if nums[mid] > nums[rp]:
                lp = mid + 1
            else:
                rp = mid
        return nums[lp]
            
            