class Solution(object):
    def characterReplacement(self, s, k):
        count = {}
        res = 0
        lp = 0
        
        for rp in range(len(s)):
            count[s[rp]] = 1 + count.get(s[rp], 0)
            
            while (rp - lp + 1) - max(count.values()) > k:
                count[s[lp]] -= 1
                lp += 1

            res = max(res, rp - lp + 1)

        return res
