class Solution(object):
    def sortColors(self, nums):
        
        for i in range(len(nums)):
            mi = 5
            index = -1
            for j in range(i+1, len(nums)):
                if nums[j] < mi:
                    mi = nums[j]
                    index = j
            if nums[index] <= nums[i]:
                temp = nums[i]
                nums[i] = mi
                nums[index] = temp
        return nums


        