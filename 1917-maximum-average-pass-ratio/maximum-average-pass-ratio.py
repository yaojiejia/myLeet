class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        d = []

        for i,c in enumerate(classes):
            old_ratio = (c[0]) / (c[1])
            new_ratio = (c[0] + 1) / (c[1] + 1)
            heapq.heappush(d,[-(new_ratio-old_ratio), i])
            
        while extraStudents != 0:
            gain, i = heapq.heappop(d)
            classes[i][0] += 1
            classes[i][1] += 1

            old_gain = classes[i][0] / classes[i][1]
            new_gain = (classes[i][0] + 1) / (classes[i][1] + 1)

            heapq.heappush(d, [-(new_gain - old_gain), i])
            extraStudents -= 1
        
        res = 0
        for p, t in classes:
            res += p/t
        return res / len(classes)
