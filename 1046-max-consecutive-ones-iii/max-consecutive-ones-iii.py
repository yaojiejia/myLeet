class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # if count of 1s - count of 0's <= k then its valid

        one_cnt = 0
        zero_cnt = 0
        lp = 0
        res = 0

        for rp in range(len(nums)):
            if nums[rp] == 1:
                one_cnt += 1
            else:
                zero_cnt += 1
            
            while zero_cnt > k:
                if nums[lp] == 1:
                    one_cnt -= 1
                else:
                    zero_cnt -= 1
                lp += 1
            print(f"lp: {lp}, rp: {rp}")
            res = max(res, rp-lp+1)
        return res