class Solution(object):
    def insert(self, intervals, newInterval):
        res = []
        stack = []
        
        # Push all intervals to the stack in reverse order
        for i in range(len(intervals) - 1, -1, -1):
            stack.append(intervals[i])
        
        # Process the intervals in the stack
        while stack:
            temp1 = stack.pop()
            if newInterval[1] < temp1[0]:  # New interval comes before the current interval
                res.append(newInterval)
                res.append(temp1)
                newInterval = None
                break
            elif newInterval[0] > temp1[1]:  # New interval comes after the current interval
                res.append(temp1)
            else:  # There is an overlap, merge intervals
                newInterval = [min(temp1[0], newInterval[0]), max(temp1[1], newInterval[1])]
        
        if newInterval:
            res.append(newInterval)
        
        # Append the remaining intervals in the stack
        while stack:
            res.append(stack.pop())
        
        # The result might be in reverse order, so reverse it
        return res

        