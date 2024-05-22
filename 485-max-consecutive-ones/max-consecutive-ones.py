class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxcount = 0
        count = 0
        length = len(nums)
        for i in range(length):
            if nums[i] == 1:
                count += 1
            if nums[i] == 0:
                maxcount = max(count, maxcount)
                count = 0
            
        return max(count, maxcount)
                
        