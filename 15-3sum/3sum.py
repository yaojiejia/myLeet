from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # Skip duplicates at the main index

            lp = i + 1
            rp = n - 1

            while lp < rp:
                temp = nums[i] + nums[lp] + nums[rp]
                if temp == 0:
                    res.append([nums[i], nums[lp], nums[rp]])
                    lp += 1
                    rp -= 1
                    # Skip duplicates at the left pointer
                    while lp < rp and nums[lp] == nums[lp - 1]:
                        lp += 1
                    # Skip duplicates at the right pointer
                    while lp < rp and nums[rp] == nums[rp + 1]:
                        rp -= 1
                elif temp < 0:
                    lp += 1
                else:
                    rp -= 1

        return res
