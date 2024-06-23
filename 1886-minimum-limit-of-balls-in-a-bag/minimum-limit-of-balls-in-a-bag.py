class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        lp, rp = 1, max(nums)
        res = rp
        while lp <= rp:
            mid = lp + (rp - lp) // 2
            temp = 0
            for n in nums:
                temp += (n - 1) // mid
            if temp <= maxOperations:
                res = mid
                rp = mid - 1
            else:
                lp = mid + 1
        return res

