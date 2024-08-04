class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        # Memoization array to store the maximum subarray sum ending at each index
        memo = [0] * n
        memo[0] = nums[0]

        for i in range(1, n):
            memo[i] = max(nums[i], memo[i-1] + nums[i])

        # The result is the maximum value in the memoization array
        return max(memo)
