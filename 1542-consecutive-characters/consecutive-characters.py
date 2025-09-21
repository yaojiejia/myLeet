class Solution:
    def maxPower(self, s: str) -> int:
        last = s[0]
        m = 1
        c = 1
        if len(s) == 1:
            return 1
        for i in range(len(s)-1):
            if s[i+1] == last:
                c += 1
                m = max(m, c)
            else:
                last = s[i+1]
                c = 1
        return m