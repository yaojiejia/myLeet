class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        
        # Count where a pair starts
        pair = [False] * n
        for i in range(1, n):
            if s[i] == s[i-1]:
                pair[i] = True
        
        res = 0
        lp = 0
        pair_count = 0
        
        for rp in range(n):
            if pair[rp]:
                pair_count += 1
            while pair_count > 1:
                if pair[lp+1]:  # move out of a pair when left passes its start
                    pair_count -= 1
                lp += 1
            res = max(res, rp - lp + 1)
        
        return res
