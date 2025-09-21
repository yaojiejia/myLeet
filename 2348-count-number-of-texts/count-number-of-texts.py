class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = 10**9 + 7
        cache = {}
        n = len(pressedKeys)

        def f(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if i in cache:
                return cache[i]

            total = f(i + 1)

            if i + 1 < n and pressedKeys[i+1] == pressedKeys[i]:
                total += f(i + 2)
            if i + 2 < n and pressedKeys[i+1] == pressedKeys[i] and pressedKeys[i+2] == pressedKeys[i]:
                total += f(i + 3)
            if pressedKeys[i] in "79" and i + 3 < n and pressedKeys[i+1] == pressedKeys[i] and pressedKeys[i+2] == pressedKeys[i] and pressedKeys[i+3] == pressedKeys[i]:
                total += f(i + 4)

            cache[i] = total % MOD
            return cache[i]

        return f(0)
