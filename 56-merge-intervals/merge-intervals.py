class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        intervals.sort()
        for interval in intervals:
            if stack and interval[0] <= stack[-1][1]:
                temp = stack.pop()
                merged_interval = [min(temp[0], interval[0]), max(temp[1], interval[1])]
                stack.append(merged_interval)
            else:
                stack.append(interval)
        return stack

