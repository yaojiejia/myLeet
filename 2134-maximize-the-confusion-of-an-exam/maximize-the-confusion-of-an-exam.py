class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        tCount = 0
        fCount = 0
        res = 0
        lp = 0
        length = len(answerKey)

        for rp in range(length):
            if answerKey[rp] == 'T':
                tCount += 1
            if answerKey[rp] == 'F':
                fCount += 1
            
            while (rp - lp + 1) - max(tCount, fCount) > k:
                if answerKey[lp] == 'T':
                    tCount -= 1
                if answerKey[lp] == 'F':
                    fCount -= 1
                lp += 1
            res = max(res, rp - lp +1)
        return res
                
        