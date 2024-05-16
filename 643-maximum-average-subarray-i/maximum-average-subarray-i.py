class Solution(object):
    def findMaxAverage(self, nums, k):
        starting = sum(nums[:k])
        max_average = starting / float(k)

        for i in range(k, len(nums)):
            starting += nums[i] - nums[i - k]
            max_average = max(max_average, starting / float(k))

        return max_average
