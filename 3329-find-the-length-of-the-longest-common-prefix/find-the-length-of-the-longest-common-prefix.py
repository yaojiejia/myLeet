class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = list(map(str, arr1))
        arr2 = list(map(str, arr2))

        prefix_map = set()

        for arr in arr1:
            prefix = ""
            for c in arr:
                prefix += c
                if prefix in prefix_map:
                    continue
                else:
                    prefix_map.add(prefix)
        
        res = 0
        for arr in arr2:
            prefix = ""
            for c in arr:
                prefix += c
                if prefix in prefix_map:
                    res = max(res, len(prefix))
        return res