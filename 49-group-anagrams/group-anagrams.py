class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)

        for s in strs:
            temp = "".join(sorted(s))
            m[temp].append(s)
        ans = []
        
        for k, values in m.items():
            ans.append(values)
        return ans