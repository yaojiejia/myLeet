class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        c1 = Counter(word1)
        c2 = Counter(word2)  
        for key in c1:
            if key not in c2:
                return False
        for key in c2:
            if key not in c1:
                return False

        cf1 = Counter(c1.values())
        cf2 = Counter(c2.values())

        return c1 == c2 or cf1 == cf2

