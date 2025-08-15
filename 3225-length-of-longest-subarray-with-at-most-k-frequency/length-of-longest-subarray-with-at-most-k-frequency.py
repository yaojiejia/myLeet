class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        c = defaultdict(int)

        res = 0
        lp = 0

        for rp in range(len(nums)):
            c[nums[rp]] += 1
            while c[nums[rp]] > k:
                c[nums[lp]] -= 1
                if c[nums[lp]] == 0:
                    del c[nums[lp]]
                lp += 1
            res = max(res, rp-lp+1)
        print(c)
        return res