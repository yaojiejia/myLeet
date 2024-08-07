class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        res = set()

        for c in sentence:
            if 'a' <= c <= 'z':
                res.add(c)
        
        if len(res) == 26:
            return True
        return False