class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        def helper(w1,w2):
            temp = False
            if w1 == w2:
                return True
            if (w1 in w2[:len(w1)]) and (w1 in w2[len(w2)-len(w1) :]):
                temp = True
            return temp
        res = 0

        for i in range(len(words)):
            for k in range(i + 1, len(words)):
                if helper(words[i],words[k]):
                    res += 1
                    print(i)
                    print(k)
        return res