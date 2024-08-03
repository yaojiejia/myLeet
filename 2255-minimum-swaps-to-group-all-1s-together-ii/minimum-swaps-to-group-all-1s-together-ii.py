class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        maxOne = nums.count(1)
        extend = nums + nums
        minZero = float('inf')
        curZero = 0

        for i in range(maxOne):
            if extend[i] == 0:
                curZero += 1
        minZero = curZero

        for i in range(maxOne, len(extend)):
            if extend[i] == 0:
                curZero += 1
            if extend[i - maxOne] == 0:
                curZero -= 1
            minZero = min(minZero, curZero)
        return minZero
            
            
