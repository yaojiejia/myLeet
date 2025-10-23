class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            lp = i+1
            rp = n - 1

            while lp < rp:
                if nums[i] + nums[lp] + nums[rp] == 0:
                    res.append([nums[i], nums[lp], nums[rp]])
                    rp -= 1
                    lp += 1

                    while lp < rp and nums[rp+1] == nums[rp]:
                        rp -= 1
                    while lp < rp and nums[lp-1] == nums[lp]:
                        lp += 1
                elif nums[i] + nums[lp] + nums[rp] > 0:
                    rp -= 1
                else:
                    lp += 1
                
        return res
