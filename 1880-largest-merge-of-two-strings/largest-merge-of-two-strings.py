class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ptr1 = 0
        ptr2 = 0
        res = ""
        while ptr1 < len(word1) and ptr2 < len(word2):
            if word1[ptr1:] >= word2[ptr2:]:
                res += word1[ptr1]
                ptr1 += 1
            else:
                res += word2[ptr2]
                ptr2 += 1
        
        if ptr1 < len(word1):
            res += word1[ptr1:]
        if ptr2 < len(word2):
            res += word2[ptr2:]
        return res
                