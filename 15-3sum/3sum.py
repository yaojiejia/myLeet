class Solution(object):
    def threeSum(self, nums):
        ans = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                lp = i + 1
                rp = len(nums) - 1
                while lp < rp:
                    temp = nums[lp] + nums[rp] + nums[i]
                    if temp < 0:
                        lp += 1
                    elif temp > 0:
                        rp -= 1
                        
                    else:
                        ans.append([nums[i],nums[lp],nums[rp]])
                        lp += 1
                        rp -= 1
                        while nums[lp] == nums[lp - 1] and lp < rp:
                            lp += 1
                        while nums[rp] == nums[rp + 1] and lp < rp:
                            rp -= 1

        
        return ans
        