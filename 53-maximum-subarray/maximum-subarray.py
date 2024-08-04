class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        memo = [0] * n
        memo[0] = nums[0]

        for i in range(1, n):
            memo[i] = max(nums[i], memo[i-1] + nums[i])

        return max(memo)
