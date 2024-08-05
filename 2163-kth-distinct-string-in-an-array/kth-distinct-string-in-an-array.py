class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        cnt = 0 
        res = ""
        for key in count:
            if count[key] == 1:
                cnt += 1
                if cnt == k:
                    res = key
        return res

