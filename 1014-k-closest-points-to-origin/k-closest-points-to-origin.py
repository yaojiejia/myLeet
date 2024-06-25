
class Solution(object):
    def kClosest(self, points, k):
        maxHeap = []
        
        for x, y in points:
            dist = -(x*x + y*y)  
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (dist, [x, y]))
            else:
                heapq.heappushpop(maxHeap, (dist, [x, y]))
        
        return [point for (dist, point) in maxHeap]