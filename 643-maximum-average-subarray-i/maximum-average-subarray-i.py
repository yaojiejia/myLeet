class Solution(object):
    def findMaxAverage(self, nums, k):
        starting = sum(nums[:k])
        max_average = starting / float(k)

        for i in range(1, len(nums) - k + 1):
            starting += nums[i + k - 1] - nums[i - 1]
            max_average = max(max_average, starting / float(k))
        
        return max_average
