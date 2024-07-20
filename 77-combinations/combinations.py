class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        z = k
        def dfs(i, curr):
            if len(curr) == z:
                res.append(curr.copy())
                return
            for k in range(i, n+1):
                curr.append(k)
                dfs(k+1,curr)
                curr.pop()
        dfs(1,[])
        return res
