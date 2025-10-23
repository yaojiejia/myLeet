class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        m = 0
        mi = float('inf')
        for log in logs:
            temp = max(log)
            temp_m = min(log)
            m = max(m, temp)
            mi = min(mi, temp_m)
        diff = m - mi
        year = [0] * (diff+1)
        for log in logs:
            print(log)
            for i in range(log[0], log[1]):
                print(i)
                year[i-mi] += 1
        ma = max(year)

        for i in range(len(year)):
            if year[i] == ma:
                return mi+i