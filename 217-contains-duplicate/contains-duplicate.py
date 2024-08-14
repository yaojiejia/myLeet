class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        print(count)
        for c in count:
            if count[c] >= 2:
                return True
        return False