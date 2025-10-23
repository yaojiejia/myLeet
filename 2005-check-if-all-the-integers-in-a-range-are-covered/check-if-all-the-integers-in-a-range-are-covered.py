class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        m = set()
        for i in range(left, right+1):
            m.add(i)
        
        ranges.sort()
        for r in ranges:
            for i in range(r[0], r[1]+1):
                if i in m:
                    if r[0] <= i and i <= r[1]:
                        m.remove(i)
        print(m)
        return False if m else True
        