class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
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
        curr.endOfWord = True
        curr.word = word

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.endOfWord


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        ROWS = len(board)
        COLS = len(board[0])

        trie = Trie()

        for word in words:
            trie.add(word)

        res = []

        def dfs(r, c, curr):

            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return
            if board[r][c] not in curr.children:
                return

            curr = curr.children[board[r][c]]

            if curr.endOfWord and curr.word not in res:
                res.append(curr.word)
            
            # Marking current cell as visited
            temp = board[r][c]
            board[r][c] = '.'
            # Explore 4 directions
            dfs(r - 1, c, curr)
            dfs(r + 1, c, curr) 
            dfs(r, c - 1, curr)
            dfs(r, c + 1, curr)

            # Backtrack
            board[r][c] = temp


        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root)

        return res

        


