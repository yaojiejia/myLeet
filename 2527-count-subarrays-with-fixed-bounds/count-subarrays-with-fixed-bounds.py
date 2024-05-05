class Solution:
    def countSubarrays(self, nums, minK, maxK):
        n = len(nums)
        ans = 0
        min_i = max_i = waste_i = -1
        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                waste_i = i
            if nums[i] == minK:
                min_i = i
            if nums[i] == maxK:
                max_i = i
            temp = min(max_i, min_i) - waste_i
            ans += max(0, temp)
        return ans