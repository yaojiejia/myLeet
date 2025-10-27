class Solution:
    def maxDepth(self, s: str) -> int:
        temp = 0
        res = 0
        for i in s:
            if i == "(":
                temp += 1
            if i == ")":
                temp -= 1
            res = max(res, temp)
        return res