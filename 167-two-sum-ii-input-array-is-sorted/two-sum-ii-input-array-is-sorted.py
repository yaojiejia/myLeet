class Solution(object):
    def twoSum(self, numbers, target):
        lp = 0
        rp = len(numbers)-1
        while lp < rp:
            temp = numbers[lp] + numbers[rp]
            if temp == target:
                return [lp+1, rp+1]
            elif temp > target:
                rp -= 1
            else:
                lp += 1
        return [0]