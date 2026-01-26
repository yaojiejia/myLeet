class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        lp = 0
        for rp in range(len(nums)-1,-1,-1):
            ans = max(ans, nums[lp] + nums[rp])
            lp += 1

        return ans