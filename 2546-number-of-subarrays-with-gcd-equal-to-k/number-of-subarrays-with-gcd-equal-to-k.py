class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            temp = nums[i]
            for j in range(i, len(nums)):
                temp = math.gcd(temp,nums[j])
                if temp == k:
                    res += 1
                elif temp < k:
                    break
        return res
