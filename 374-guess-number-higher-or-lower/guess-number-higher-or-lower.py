# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        
        lp = 0
        rp = n-1

        while lp<=rp:
            mid = (lp+rp) //2
            g = guess(mid)
            if g == 0:
                return mid
            
            if g == -1:
                rp = mid - 1
            else:
                lp = mid + 1
        return lp