class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        array = [[] for _ in range(numRows)]
        i = 0
        direction = 1
        for c in s:
            if direction == 1:
                array[i].append(c)
                i += 1
            elif direction == -1:
                array[i].append(c)
                i -= 1
            if i == numRows - 1:
                direction = -1
            if i == 0:
                direction = 1
        res = ''.join(''.join(row) for row in array)
        return res