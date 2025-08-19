class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0

        streak = 0
        for i, n in enumerate(nums):
            if n == 0:
                streak += 1
            else:
                res += streak * (streak + 1) // 2
                streak = 0
            if i == len(nums) - 1:
                res += streak * (streak + 1) // 2
        return res