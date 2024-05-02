class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s == "":
            return 0
        if s == " ":
            return 1
        if len(s) == 1:
            return 1
        maxWord = ""
        word = s[0]

        for i in range(1, len(s)):
            char = s[i]
            if char in word:
                if len(word) > len(maxWord):
                    maxWord = word
                index = word.index(char)
                word = word[index+1:] + char
            else:
                word += char

        return max(len(word), len(maxWord))
            

            
        