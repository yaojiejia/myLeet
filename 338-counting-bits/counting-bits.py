class Solution(object):
    def countBits(self, n):
        output = []
        for i in range(n + 1):
            value = bin(i).count("1")
            output.append(value)
        return output
        