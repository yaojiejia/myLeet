class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def helper(num, target):
            lp = 0
            rp = len(num) - 1

            while lp <= rp:
                mid = (rp+lp) // 2
                if num[mid] < target:
                    lp = mid + 1
                else:
                    rp = mid - 1
            return lp
        first = helper(nums, target)
        if first == len(nums) or nums[first] != target:
            return [-1,-1]
        last = helper(nums, target+1)-1

        return [first, last]  