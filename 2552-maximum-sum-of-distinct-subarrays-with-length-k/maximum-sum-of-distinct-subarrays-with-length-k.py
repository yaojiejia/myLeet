from collections import Counter
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        lp = 0
        res = 0
        count = Counter()
        current_sum = 0

        for rp in range(len(nums)):
            count[nums[rp]] += 1
            current_sum += nums[rp]

            # Check if the window has reached size k
            if rp - lp + 1 == k:
                # Check if all elements in the window are unique
                if len(count) == k:
                    res = max(res, current_sum)
                
                # Slide the window by moving the left pointer
                count[nums[lp]] -= 1
                current_sum -= nums[lp]
                if count[nums[lp]] == 0:
                    del count[nums[lp]]
                lp += 1

        return res
