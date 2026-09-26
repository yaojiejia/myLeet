class Solution:
    def minimizeResult(self, expression: str) -> str:
        l, r = expression.split('+')
        best, ans = float('inf'), ""
        for i in range(len(l)):
            for j in range(1, len(r) + 1):
                a = int(l[:i]) if i else 1
                b = int(l[i:])
                c = int(r[:j])
                d = int(r[j:]) if j < len(r) else 1
                val = a * (b + c) * d
                if val < best:
                    best = val
                    ans = f"{l[:i]}({l[i:]}+{r[:j]}){r[j:]}"
        return ans