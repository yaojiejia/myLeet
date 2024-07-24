class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dp (i, curr):
            if i >= len(nums):
                if curr not in res:
                    res.append(curr.copy())
                return
            
            curr.append(nums[i])
            dp(i+1, curr)
            curr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
                dp(i + 1, curr)
            dp(i+1, curr)
        
        dp(0,[])
        return res