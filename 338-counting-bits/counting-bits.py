class Solution(object):
    def countBits(self, n):
        ans = []
        for i in range(0, n+1):
            ans.append(self.hammingWeight(i))
        
        return ans
        
        
    def hammingWeight(self, n):
        binary = bin(n)
        st = str(binary)
        count = 0
        for i in range(0, len(st)):
            if st[i] == '1':
                count+=1
        
        return count