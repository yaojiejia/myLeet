class Solution(object):
    def shipWithinDays(self, weights, days):
        lp = max(weights)  # minimum capacity should be at least the heaviest package
        rp = sum(weights)  # maximum capacity would be the sum of all weights
        res = rp
        
        while lp <= rp:
            mid = lp + (rp - lp) // 2
            temp2 = 1
            current_sum = 0
            
            for weight in weights:
                if current_sum + weight > mid:
                    temp2 += 1
                    current_sum = weight
                else:
                    current_sum += weight
            
            if temp2 <= days:
                res = mid
                rp = mid - 1
            else:
                lp = mid + 1
        
        return res
