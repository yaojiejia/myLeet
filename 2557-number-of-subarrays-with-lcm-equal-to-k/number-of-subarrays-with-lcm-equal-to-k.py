class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            temp = nums[i]
            for j in range(i, n):
                temp = math.lcm(temp, nums[j])
                if temp == k:
                    res += 1
                if k < temp:
                    break
        return res