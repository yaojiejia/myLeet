from typing import List

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        s_n = len(s)
        a_n = len(a)
        b_n = len(b)

        a_idx = []
        b_idx = []
        for i in range(s_n - a_n + 1):
            if s[i:i+a_n] == a:
                a_idx.append(i)
        for i in range(s_n - b_n + 1):
            if s[i:i+b_n] == b:
                b_idx.append(i)
        a_idx.sort()
        b_idx.sort()
        
        result = []
        if not b_idx:
            return result

        for idx in a_idx:
            # binary search insertion point for idx in b_idx
            lp, rp = 0, len(b_idx) - 1
            pos = len(b_idx)  # first >= idx (lower_bound)
            while lp <= rp:
                mid = (lp + rp) // 2
                if b_idx[mid] >= idx:
                    pos = mid
                    rp = mid - 1
                else:
                    lp = mid + 1

            ok = False
            # candidate on the right (>= idx)
            if pos < len(b_idx) and abs(b_idx[pos] - idx) <= k:
                ok = True
            # candidate on the left (< idx)
            if pos - 1 >= 0 and abs(b_idx[pos - 1] - idx) <= k:
                ok = True

            if ok:
                result.append(idx)

        return result
