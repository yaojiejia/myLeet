class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        # monotonically increasing
        # [3,5,2] k = 2
        # [3,5,2,6] k = 3
        n = len(nums) # 8
        for i, num in enumerate(nums):
            while stack and stack[-1] > num and (len(stack) + n-i) > k: 
                stack.pop()
            if len(stack) < k:
                stack.append(num)
        return stack