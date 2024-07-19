import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(heap)
        res = []
        prev_freq, prev_char = 0, ''
        
        while heap:
            freq, char = heapq.heappop(heap)
            res.append(char)
            
            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_char))
            
            prev_freq, prev_char = freq + 1, char
        
        res = ''.join(res)
        return res if len(res) == len(s) else ""