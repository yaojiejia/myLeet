class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]  # slice after breaking

        res = ""
        for i in range(len(s)):
            # odd-length palindrome
            tmp = expand(i, i)
            if len(tmp) > len(res):
                res = tmp
            # even-length palindrome
            tmp = expand(i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res
