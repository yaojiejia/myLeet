class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        count, window = {}, {}
        for x in t:
            count[x] = 1 + count.get(x, 0)
        
        have, need = 0, len(count)
        res = [-1, -1]
        res_len = float('inf')
        
        lp = 0
        for rp in range(len(s)):
            temp = s[rp]
            window[temp] = 1 + window.get(temp, 0)
            
            if temp in count and window[temp] == count[temp]:
                have += 1
            
            while have == need:
                if (rp - lp + 1) < res_len:
                    res = [lp, rp]
                    res_len = rp - lp + 1
                
                window[s[lp]] -= 1
                if s[lp] in count and window[s[lp]] < count[s[lp]]:
                    have -= 1
                lp += 1 
        
        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""
