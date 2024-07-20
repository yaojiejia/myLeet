class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        count = Counter(nums)
        def bt():
            if len(cur) == len(nums):
                res.append(cur.copy())
                return 
            
            for n in count:
                if count[n] > 0:
                    cur.append(n)
                    count[n] -=1
                    bt()
                    count[n] += 1
                    cur.pop()
                    
        
        bt()
        return res