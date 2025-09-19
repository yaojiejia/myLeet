from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c = Counter(s)
        stack = []
        window = set()
        for char in s:
            c[char] -= 1

            if char in window:
                continue
            while stack and stack[-1] > char and c[stack[-1]] > 0:
                rm = stack.pop()
                window.remove(rm)

            if char not in window:
                stack.append(char)
                window.add(char)
        return "".join(stack)
