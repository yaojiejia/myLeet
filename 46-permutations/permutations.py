class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(cur):
            if len(cur) == len(nums):
                ans.append(cur.copy())
                return
            for n in nums:
                if n in cur: continue
                cur.append(n)
                backtrack(cur)
                cur.pop()
        backtrack([])
        return ans