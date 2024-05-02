class Solution(object):
    def hammingWeight(self, n):
        binary = bin(n)
        st = str(binary)
        count = 0
        for i in range(0, len(st)):
            if st[i] == '1':
                count+=1
        
        return count

        