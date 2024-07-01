class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        return max(self.helper(nums[1:]),self.helper(nums[0:-1]))

    def helper(self,nums):
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])

        res = [0]*len(nums)
        
        res[0] = nums[0]
        res[1] = max(nums[0],nums[1])

        for i in range(1,len(res)-1):
            res[i+1] = max((nums[i+1] + res[i-1]),res[i])
            print(res[i+1])
        return res[len(res)-1]
        