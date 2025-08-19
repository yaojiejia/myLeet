class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        def convertMin(t):
            h, m = t.split(":")
            return int(h) * 60 + int(m)

        mins = [convertMin(t) for t in timePoints]
        mins.sort()

        min_diff = float("inf")
        for i in range(1, len(mins)):
            min_diff = min(min_diff, mins[i] - mins[i-1])

        # check wrap-around (last to first across midnight)
        min_diff = min(min_diff, 24*60 - (mins[-1] - mins[0]))

        return min_diff
