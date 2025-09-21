class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        powers = []
        i = 1
        while i**x <= n:
            p = i**x
            powers.append(p)
            i += 1

        dp = [0] * (n + 1)
        dp[0] = 1

        for p in powers:
            for t in range(n, p - 1, -1):
                dp[t] = (dp[t] + dp[t - p]) % MOD

        return dp[n]