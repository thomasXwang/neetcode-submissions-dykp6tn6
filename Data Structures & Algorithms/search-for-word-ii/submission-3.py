class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        ROWS = len(board)
        COLS = len(board[0])

        res = set()

        trie = Trie()
        for word in words:
            trie.add(word)

        def dfs(r, c, curr):

            if curr.word:
                res.add(curr.word)

            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return

            if board[r][c] not in curr.children:
                return

            curr = curr.children[board[r][c]]

            tmp = board[r][c]
            board[r][c] = '.'
        
            dfs(r - 1, c, curr)
            dfs(r + 1, c, curr)
            dfs(r, c - 1, curr)
            dfs(r, c + 1, curr)

            board[r][c] = tmp

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in trie.root.children:
                    dfs(r, c, trie.root)
        return list(res)
