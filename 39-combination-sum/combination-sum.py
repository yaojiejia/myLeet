class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        curr = []
        res = []
        
        def f(i, total):
            if total == target:
                res.append(curr[:])
                return
            if total > target:
                return
            
            for x in range(i, len(candidates)):
                curr.append(candidates[x])
                f(x, total + candidates[x])   # allow reuse of same number
                curr.pop()
        
        f(0, 0)
        return res
