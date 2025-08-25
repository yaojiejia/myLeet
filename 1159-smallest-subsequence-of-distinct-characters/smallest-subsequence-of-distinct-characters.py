class Solution:
    def smallestSubsequence(self, s: str) -> str:
        c = Counter(s)
        stack = []
        visited = set()
        # abcc
        # only pop if 
        for char in s:
            c[char] -= 1
            if char in visited:
                continue
            while stack and stack[-1] > char and c[stack[-1]] > 0:
                temp = stack.pop()
                visited.remove(temp)
            stack.append(char)
            visited.add(char)
        return "".join(stack)