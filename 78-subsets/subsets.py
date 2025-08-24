class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        curr = []
        n = len(nums)

        def f(i):
            if i == n:
                res.append(curr[:])
                return
            # we dont choose current element and move to next
            f(i+1)

            # we choose current element and move to next
            curr.append(nums[i])
            f(i+1)
            curr.pop()
        f(0)
        return res