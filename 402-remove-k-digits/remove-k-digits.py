class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # remove the largest digit? 
        # need to check the tail of stack if it is 0
        # if 0 and curr is 0, then dont touch curr 0
        stack = []
        n = len(num)
        # can have at most len(num) - k digits
        m = n-k
        # 122219 m = 4, n = 6, l = 4 i = 3

        for i, char in enumerate(num):
            while stack and stack[-1] > int(char) and len(stack) + (n-i) > m:
                stack.pop()

            if len(stack) < m:
                stack.append(int(char))
        res = ""
        for i, char in enumerate(stack):
            res += str(char)
        res = res.lstrip("0")
        return res if res else "0"
        