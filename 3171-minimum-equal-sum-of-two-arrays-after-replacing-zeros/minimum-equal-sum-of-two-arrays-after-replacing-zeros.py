class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        n1_sum = sum(nums1)
        n2_sum = sum(nums2)
        
        n1_zero_cnt = nums1.count(0)
        n2_zero_cnt = nums2.count(0)

        if n1_zero_cnt == 0 and n2_zero_cnt == 0:
            if n1_sum == n2_sum:
                return n1_sum
            else:
                return -1

        # Case 1: nums1 has no zeros
        if n1_zero_cnt == 0:
            if n2_sum + n2_zero_cnt <= n1_sum:
                return n1_sum
            else:
                return -1

        # Case 2: nums2 has no zeros
        if n2_zero_cnt == 0:
            if n1_sum + n1_zero_cnt <= n2_sum:
                return n2_sum
            else:
                return -1
        # Case 3: both have zeros
        if n1_sum + n1_zero_cnt >= n2_sum + n2_zero_cnt:
            return n1_sum + n1_zero_cnt
        else:
            return n2_sum + n2_zero_cnt
