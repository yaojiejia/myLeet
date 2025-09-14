from typing import List

class Solution:
    def seePeople(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        res = [[0] * n for _ in range(m)]
        
        # Horizontal pass (right to left)
        for i in range(m):
            stack = []
            for j in range(n - 1, -1, -1):
                current_height = heights[i][j]
                
                # Count all shorter people we can see
                while stack and heights[i][stack[-1]] < current_height:
                    stack.pop()
                    res[i][j] += 1
                
                # Handle equal or taller person
                if stack:
                    if heights[i][stack[-1]] == current_height:
                        stack.pop()  # Remove equal height person (we see through them)
                    res[i][j] += 1  # Count one person (equal or taller)
                
                stack.append(j)
        
        # Vertical pass (bottom to top)
        for j in range(n):
            stack = []
            for i in range(m - 1, -1, -1):
                current_height = heights[i][j]
                
                # Count all shorter people we can see
                while stack and heights[stack[-1]][j] < current_height:
                    stack.pop()
                    res[i][j] += 1
                
                # Handle equal or taller person
                if stack:
                    if heights[stack[-1]][j] == current_height:
                        stack.pop()  # Remove equal height person (we see through them)
                    res[i][j] += 1  # Count one person (equal or taller)
                
                stack.append(i)
        
        return res