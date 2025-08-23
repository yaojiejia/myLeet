from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def isPalindrome(t: str) -> bool:
            return t == t[::-1]

        n = len(s)

        def f(s_i: int):
            if s_i == n:
                res.append(curr[:])
                return

            # try all substrings starting at s_i
            for i in range(s_i, n):
                sub = s[s_i:i+1]         # contiguous substring
                if isPalindrome(sub):    # only proceed if palindrome
                    curr.append(sub)
                    f(i + 1)
                    curr.pop()

        f(0)
        return res
