class Solution(object):
    def singleNumber(self, nums):
        hash = Counter(nums)

        for x in hash:
            if hash[x] == 1:
                return x
        return -1
        