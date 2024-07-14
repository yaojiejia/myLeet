class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ex = (n*(n+1)) // 2
        su = 0
        du = 0
        ma = {}
        for num in nums:
            if num in ma:
                du = num
                break
            else:
                ma[num] = 10
        for num in nums:
            su += num
        return [du, ex - su + du]