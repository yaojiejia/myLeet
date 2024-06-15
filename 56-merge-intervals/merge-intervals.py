class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        res = []
        stack = []
        for i in range(len(intervals) - 1, -1, -1):
            stack.append(intervals[i])

        while stack:
            temp = stack.pop()
            if not stack:
                res.append(temp)
                break
            temp2 = stack.pop()
            if temp[1] >= temp2[0]: 
                merged = [min(temp[0], temp2[0]), max(temp[1], temp2[1])]
                stack.append(merged)
            else:
                res.append(temp)
                stack.append(temp2)
        return res


        