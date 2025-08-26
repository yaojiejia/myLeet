class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # if len(nums) == 1 and nums[0] == 0:
        #     return False
        prefix = 0
        m = {0:-1}
        for i, num in enumerate(nums):
            prefix += num
            temp = prefix % k
            
            if temp in m:
                if i - m[temp] >= 2:
                    return True
            else:
                m[temp] = i
        
        return False
            