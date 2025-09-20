class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        ans = 0
        lp = 0
        lp_char = s[0]

        for rp in range(len(s)-1):
            if s[rp+1] != lp_char:
                n = (rp-lp+1)
                ans += (n*(n+1)) // 2
                ans %= MOD
                lp = rp + 1
                lp_char = s[rp+1]
        n = (len(s) - lp)
        ans += (n*(n+1)) // 2
        return ans % MOD
        
            