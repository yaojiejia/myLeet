class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = 10000000000
        for i in range(0,len(arr)-1):
            min_diff = min(min_diff, abs(arr[i+1] - arr[i]))
        res = []
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == min_diff:
                res.append([arr[i], arr[i+1]])
        return res
        