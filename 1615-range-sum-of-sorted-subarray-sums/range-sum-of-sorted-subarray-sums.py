from typing import List

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []

        for i in range(len(nums)):
            sub_sum = 0
            for j in range(i, len(nums)):
                sub_sum += nums[j]
                res.append(sub_sum)
        
       
        res.sort()
        
       
        return sum(res[left-1:right]) % (10**9 + 7)