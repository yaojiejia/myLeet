class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs = sorted(strs, key=len)

        loop = strs[0]
        res = ""
        for i in range(len(loop)):
            curr = loop[i]
            cond = True
            for j in range(1,len(strs)):
                if strs[j][i] != curr:
                    cond = False
                    break
            if cond:
                res += curr
            else:
                break
        return res
