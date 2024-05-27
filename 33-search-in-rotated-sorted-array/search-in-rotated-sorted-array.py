class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # Check if the left half is sorted
            if nums[l] <= nums[m]:
                # If target is within the range of the sorted left half
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # Else the right half must be sorted
            else:
                # If target is within the range of the sorted right half
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
