from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0 and abs(asteroid) > abs(stack[-1]):
                stack.pop()
            if stack and stack[-1] > 0 and asteroid < 0 and abs(asteroid) < abs(stack[-1]):
                continue
            if stack and stack[-1] > 0 and asteroid < 0 and abs(asteroid) == abs(stack[-1]):
                stack.pop()
                continue
            stack.append(asteroid)
        return stack
