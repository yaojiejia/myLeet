# Simple Trie class to contain the words
class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.count = 0


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie_root = Trie()
        ans = 0

        for word in words:
            node = trie_root
            # consider iterating the words in first and last letter simultaneously
            # this is done to ensure to check if both prefic and suffix condition are
            # satisfied
            for start_letter, end_letter in zip(word, word[::-1]):
                # So from each first_letter, last_letter we can go to the more 
                # inner chars
                key = start_letter + "@" + end_letter
                node = node.children[key]

                # add the no. of words with same prefix and suffix as this word
                ans += node.count
            
            # increment the count as this iterated word is added to trie
            node.count += 1
        
        return ans