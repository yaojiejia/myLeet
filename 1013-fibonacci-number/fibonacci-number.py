class Solution:
    def fib(self, n: int) -> int:
        m = {}
        if n == 0:
            return 0
        def newFib(n, m):
            if n in m:
                return m[n]
            if n <= 2:
                return 1
            m[n] = newFib(n-1, m) + newFib(n-2, m)
            return m[n]
        return newFib(n,m)