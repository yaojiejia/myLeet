class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        lp = 0
        res = 0

        for rp in range(len(s)):
            while lp <= rp and s[rp] in window:
                window[s[lp]] = False
                if window[s[lp]] is False:
                    del window[s[lp]]
                lp += 1
            window[s[rp]] = True
            res = max(res,(rp-lp) + 1)
        return res