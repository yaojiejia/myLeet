class Solution(object):
    def pivotIndex(self, nums):
        left = 0
        s = sum(nums)
        
        for k in range(0, len(nums)):
            if left == (s - left - nums[k]):
                return k
            left += nums[k]
        return -1
