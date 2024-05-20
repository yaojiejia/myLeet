class Solution(object):
    def largestAltitude(self, gain):
        prefix = [0]  
        for i in range(len(gain)):
            prefix.append(prefix[-1] + gain[i]) 
        return max(prefix)
