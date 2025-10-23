class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        lp = 0
        res = 0

        for rp in range(len(s)):
            while s[rp] in m and lp < rp:
                
                del m[s[lp]]
                lp += 1
            res = max(res, (rp-lp+1))
            m[s[rp]] = rp
        return res