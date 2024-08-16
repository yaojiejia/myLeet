class Solution:
    def partitionString(self, s: str) -> int:
        count = []
        res = 1
        for i in range(len(s)):
            if s[i] not in count:
                count.append(s[i])
            else:
                res += 1
                count.clear()
                count.append(s[i])

        return res