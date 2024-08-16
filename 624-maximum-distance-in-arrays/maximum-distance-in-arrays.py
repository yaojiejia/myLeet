class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_dist = arrays[0][0]
        max_dist = arrays[0][-1]
        res = 0
        for i in range(1, len(arrays)):
            res = max(res, abs(arrays[i][-1] - min_dist), abs(max_dist - arrays[i][0]))
            max_dist = max(max_dist, arrays[i][-1])
            min_dist = min(min_dist, arrays[i][0])
        return res