from typing import List

class Solution:
    def seePeople(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        res = [[0] * n for _ in range(m)]
        
        # Horizontal pass (right to left)
        for r in range(m):
            stack = []
            for c in range(n - 1, -1, -1):
                ppl = 0
                while stack and heights[r][c] > stack[-1]:
                    stack.pop()
                    ppl += 1
                if stack:
                    if heights[r][c] == stack[-1]:
                        stack.pop()
                    ppl += 1
                res[r][c] += ppl
                stack.append(heights[r][c])
        
        # Vertical pass (bottom to top)
        for c in range(n):
            stack = []
            for r in range(m - 1, -1, -1):
                ppl = 0
                while stack and heights[r][c] > stack[-1]:
                    stack.pop()
                    ppl += 1
                if stack:
                    if heights[r][c] == stack[-1]:
                        stack.pop()
                    ppl += 1
                res[r][c] += ppl
                stack.append(heights[r][c])
        
        return res