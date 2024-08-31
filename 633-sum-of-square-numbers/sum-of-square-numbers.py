class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = ceil(math.sqrt(c))

        while a<=b:
            cur_sum = a**2 + b**2
            if cur_sum == c:
                return True
            elif cur_sum < c:
                a+=1
            else:
                b-=1
        return False