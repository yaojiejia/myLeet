class Solution(object):
    def lastStoneWeight(self, stones):
        length = len(stones)
        for i in range(length):
            stones[i] = -1 * stones[i]
        heapify(stones)
        
        while stones:
            stone1 = -heappop(stones)
            if not stones:
                return stone1
            stone2 = -heappop(stones)

            if stone1 > stone2: 
                heappush(stones, stone2 - stone1)
            
        return 0

        

        
        