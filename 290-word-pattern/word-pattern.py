class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        m = {}
        arr = s.split(" ")
        t = {}
        if len(arr) != len(pattern):
            return False
        for i in range(len(pattern)):
            if arr[i] in t:
                if t[arr[i]] != pattern[i]:
                    return False
            else:
                t[arr[i]] = pattern[i]
            
            if pattern[i] in m:
                if arr[i] != m[pattern[i]]:
                    return False
            else:
                m[pattern[i]] = arr[i]
        return True
