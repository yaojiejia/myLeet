class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
    
    def search(self, prefix):
        cur = self.root
        val = ""
        for c in prefix:
            if c not in cur.children:
                break
            val += c
            cur = cur.children[c]
            if cur.word:
                return val
        return ""

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        wordList = sentence.split(" ")
   
        res = []
        for word in wordList:
            
            temp = trie.search(word)
            if temp == "":
                res.append(word)
            else:
                res.append(temp)
        return " ".join(res)

        