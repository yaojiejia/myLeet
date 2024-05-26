class Solution(object):
    def search(self, nums, target):

        return self.BST(nums, target, 0, len(nums)-1)
        
    def BST(self, nums, target, low, high):

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
            
        