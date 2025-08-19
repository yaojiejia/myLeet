class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        n = len(nums)

        for i in range(n-1, -1, -1):
            if nums[i] in seen:
                if abs(i-seen[nums[i]]) <= k:
                    return True
            
            seen[nums[i]] = i
        return False