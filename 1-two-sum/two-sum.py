class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cond = False
        i = 0
        res = []
        while cond == False:
            temp = target - nums[i]
            for j in range(i+1, len(nums)):
                if temp == nums[j]:
                    res = [i,j]
                    cond = True
            i += 1
        return res