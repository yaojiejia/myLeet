class Solution(object):
    def minimizedMaximum(self, n, quantities):
        lp = 1
        rp = max(quantities)
        res = rp
        
        while lp <= rp:
            mid = lp + (rp - lp) // 2
            temp = 0
            for q in quantities:
                while q > 0:
                    temp += 1
                    q -= mid
            
            if temp <= n:
                res = min(res, mid)
                rp = mid - 1
            else:
                lp = mid + 1
        
        return res
