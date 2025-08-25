class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # seems like a two pointers and monotonic stack question? 

        ptr1 = 0
        ptr2 = 0
        n1 = len(nums1)
        n2 = len(nums2)
        
        def formSub(nums, m):
            stack = []
            
            for i, num in enumerate(nums):
                while stack and stack[-1] < num and (len(stack) + len(nums) - i) > m:
                    stack.pop() 

                if len(stack) < m:
                    stack.append(num)
            return stack

        def comb(c1, c2):
            p1, p2 = 0,0
            res = []
            while p1 < len(c1) and p2 < len(c2):
                if c1[p1:] >= c2[p2:]:
                    res.append(c1[p1])
                    p1 += 1
                else:
                    res.append(c2[p2])
                    p2 += 1
            if p1 < len(c1):
                res = res + c1[p1:]
            if p2 < len(c2):
                res = res + c2[p2:]
            return res
            
        res = -1
        res_comb = [-1]
        for k1 in range(k+1):
            k2 = k-k1
            # form subsequence for k1 and k2
            c1 = formSub(nums1, k1)
            c2 = formSub(nums2, k2)
            # print(f"c1: {c1} c2:{c2}")
            # combine subk1 and subk2 to find the max out of theses two
            curr_comb = comb(c1,c2)
            # print(curr_comb)
            # record the combination from above step and repeat to find the max out of all combinations
            int_comb = int("".join(map(str,curr_comb)))
            if int_comb > res:
                res = int_comb
                res_comb = curr_comb
        return res_comb
        