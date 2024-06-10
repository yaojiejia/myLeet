class Solution(object):
    def heightChecker(self, heights):
        sortedHeight = sorted(heights) 
        counter = 0
        for i in range(len(heights)):
            if heights[i] != sortedHeight[i]:
                counter += 1
        return counter
        