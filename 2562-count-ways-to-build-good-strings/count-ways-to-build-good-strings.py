class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1

        for i in range(1, high + 1):
            if i - zero >= 0:
                dp[i] += dp[i - zero]
            if i - one >= 0:
                dp[i] += dp[i - one]
            dp[i] %= MOD

        res = 0
        for i in range(low, high + 1):
            res += dp[i]
        return res % MOD
