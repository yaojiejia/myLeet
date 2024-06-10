class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        return max(nums[0],self.helper(nums[1:]), self.helper(nums[:-1]))
        
    def helper(self, nums):
        if len(nums) <= 2:
            return max(nums)
        dp = [0]*(len(nums)+1)
        dp[1] = nums[0]
        dp[2] = nums[1]
        for i in range(2, len(nums)):
            dp[i+1] = max(dp[i-1]+nums[i], dp[i-2]+nums[i])
        return max(dp)