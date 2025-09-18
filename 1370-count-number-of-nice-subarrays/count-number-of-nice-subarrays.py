from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        for rp in range(len(nums)):
            if nums[rp] % 2 == 0:
                nums[rp] = 0
            else:
                nums[rp] = 1
        
        freq = {}
        prefix = 0
        res = 0
        print(nums)
        for num in nums:
            prefix += num
            if prefix == k:
                res += 1
            if prefix - k in freq:
                res += freq[prefix - k]
            freq[prefix] = freq.get(prefix, 0) + 1
        return res