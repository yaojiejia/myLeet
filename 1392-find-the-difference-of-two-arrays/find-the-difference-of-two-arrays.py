class Solution(object):
    def findDifference(self, nums1, nums2):
        l1 = [set(nums1).difference(set(nums2))]
        l2 = [set(nums2).difference(set(nums1))]
        return l1 + l2

        