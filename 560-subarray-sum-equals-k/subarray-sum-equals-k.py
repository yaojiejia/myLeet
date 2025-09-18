class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        # if prefix - k is in freq, then is is valid
        prefix = 0
        res = 0
        for num in nums:
            prefix += num
            
            if prefix == k:
                res += 1
            
            if prefix - k in freq:
                res += freq[prefix-k]
            
            freq[prefix] = freq.get(prefix, 0) + 1
        return res