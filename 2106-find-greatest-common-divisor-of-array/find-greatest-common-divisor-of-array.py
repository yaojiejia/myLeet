class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minNum = min(nums)
        maxNum = max(nums)
        print(minNum)
        print(maxNum)
        res = 0
        for i in range(1, minNum+1):
            if maxNum % i == 0 and minNum %i == 0:
                res = max(res, i)
        return res