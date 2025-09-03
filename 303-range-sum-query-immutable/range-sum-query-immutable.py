class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        temp = 0
        for num in nums:
            temp += num
            self.prefix.append(temp)
        # [-2, -2, 1, -4, -2, -3]
        #       -      -
        # prefix[i,j] = prefix[0, j] - prefix[0, i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left-1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)