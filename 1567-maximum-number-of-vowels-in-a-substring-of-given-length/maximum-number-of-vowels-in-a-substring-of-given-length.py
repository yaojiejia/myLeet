class Solution(object):
    def maxVowels(self, s, k):
        vowel = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        maxcount = 0
        for i in range(0,k):
            if s[i] in vowel:
                count += 1
        maxcount = count

        for j in range(k,len(s)):
            if s[j] in vowel:
                count += 1
            if s[j - k] in vowel:
                count -= 1
            maxcount = max(count, maxcount)

        return maxcount

        

