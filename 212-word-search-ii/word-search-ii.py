from typing import List, Dict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        res = set()
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        
        def dfs(r, c, node, path):
            if node.end_of_word:
                res.add(path)
                node.end_of_word = False  # To avoid duplicate words
            
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                board[r][c] not in node.children or (r, c) in visited):
                return
            
            visited.add((r, c))
            next_node = node.children[board[r][c]]
            dfs(r + 1, c, next_node, path + board[r][c])
            dfs(r - 1, c, next_node, path + board[r][c])
            dfs(r, c + 1, next_node, path + board[r][c])
            dfs(r, c - 1, next_node, path + board[r][c])
            visited.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                visited = set()
                dfs(r, c, trie.root, "")
        
        return list(res)


