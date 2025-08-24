class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        res = []
        curr = []

        def f(i):
            if len(curr) == len(s):
                res.append("".join(curr[:]))
                return
            if len(curr) > len(s):
                return 
            if s[i].isalpha():
                curr.append(s[i].lower())
                f(i+1)
                curr.pop()

                curr.append(s[i].upper())
                f(i+1)
                curr.pop()
            else:
                curr.append(s[i])
                f(i+1)
                curr.pop()
        f(0)
        return res