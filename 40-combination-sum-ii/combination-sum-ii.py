class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # Sort to handle duplicates

        def bt(i, curr, t):
            if t == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or t > target:
                return
            curr.append(candidates[i])
            bt(i + 1, curr, t + candidates[i])
            curr.pop()
            
            # Skip duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            bt(i + 1, curr, t)

        bt(0, [], 0)
        return res