class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        lp = 0
        res = 1  

        for rp in range(1, len(s)):
            if ord(s[rp]) != ord(s[rp-1]) + 1:
                lp = rp
            res = max(res, rp - lp + 1)
        return res
