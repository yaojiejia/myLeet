class Solution:
    def hIndex(self, citations: List[int]) -> int:

        if len(citations) == 1:
            if citations[0] == 0:
                return 0
            else:
                return 1

        c = dict(sorted(Counter(citations).items()))
        total = len(citations)
        # 1x1 2x2 3x3 4x4 
        
        ans = 0
        for i in range(0, len(citations) + 1):
            if total >= i:
                ans = i
                if i in c:
                    total -= c[i]

        return ans            