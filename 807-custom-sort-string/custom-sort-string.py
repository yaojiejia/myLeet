class Solution:
    def customSortString(self, order: str, s: str) -> str:
        c = {}
        for i,ch in enumerate(order):
            c[ch] = i

        res = defaultdict(list)
        
        for i,ch in enumerate(s):
            if ch in c:
                res[c[ch]].append(ch) 
            else:
                res[i].append(ch)
        temp = dict(sorted(res.items()))
        result = ""

        for k, v in temp.items():
            for ch in v:
                result += ch
        return result