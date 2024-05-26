class Solution(object):
    def longestConsecutive(self, nums):

        if not nums:
            return 0
        nums = sorted(set(nums))
        maxcount = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                count += 1
            else:
                maxcount = max(count, maxcount)
                count = 1
        return max(maxcount,count)

        