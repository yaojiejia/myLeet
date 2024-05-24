class MedianFinder(object):

    def __init__(self):
        self.ans = []


    def addNum(self, num):
        self.ans.append(num)

        

    def findMedian(self):
        self.ans.sort()
        n = len(self.ans)
        if n % 2 == 1:
            return self.ans[n // 2]
        else:
            return (self.ans[(n // 2) - 1] + self.ans[n // 2]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()