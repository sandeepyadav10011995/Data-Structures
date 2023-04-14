"""
Problem 1: Word Search : Given a M*N board and a word; find if the word exits in the Grid?


Problem 2: Search words in Crosswords.

Approach 1: Use the code of Word Search and run it for every word !!

Approach 2: Using Trie

"""
from copy import deepcopy


class WordSearchSolution:
    def __init__(self):
        self.rows = None
        self.cols = None
        self.board = None

    def _getNeighbors(self, row, col):
        neighbors = []
        for rowOffset, colOffset in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            newRow, newCol = row+rowOffset, col+colOffset
            if newRow < 0 or newRow == self.rows or newCol < 0 or newCol == self.cols:
                continue
            neighbors.append((newRow, newCol))
        return neighbors

    def _dfs(self, row: int, col: int, word: str) -> bool:
        # Base Case --> Our Goal
        if not word:
            return True

        # Back-Up
        value = self.board[row][col]
        # Mark the cell as visited
        self.board[row][col] = None
        #Explore
        for nRow, nCol in self._getNeighbors(row, col):
            if self.board[nRow][nCol] == word[0] and self._dfs(nRow, nCol, word[1:]):
                return True

        # Backtrack
        self.board[row][col] = value
        return False


    def wordExists(self, board: list[list[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board
        for row in range(self.rows):
            for col in range(self.cols):
                if self._dfs(row, col, word):
                    return True


class Crossword1:  # TC: O(N*N*L) ~ O(N^2*L)
    @staticmethod
    def findWords(board: list[list[str]], words: list[str]) -> list:
        wss = WordSearchSolution()
        return [word for word in words if wss.wordExists(deepcopy(board), word)]


class Crossword2:
    def __init__(self) -> None:

        self.rows = None
        self.cols = None
        self.board = None
        self.trie = None
        self.matchedWords = None
        self.WORDKEY = "$"

    def _dfs(self, row: int, col: int) -> None:
        # Base Case --> Our Goal
        letter = self.board[row][col]
        curNode = self.trie[letter]

        wordMatch = curNode.pop(self.WORDKEY, False)
        if wordMatch:
            self.matchedWords.append(wordMatch)

        # Mark the node as visited
        self.board[row][col] = "#"
        # Explore
        for rowOffset, colOffset in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            newRow, newCol = row+rowOffset, col+colOffset
            if newRow < 0 or newRow == self.rows or newCol < 0 or newCol == self.cols:
                continue
            self._dfs(newRow, newCol)

        # Undo --> Backtrack
        self.board[row][col] = letter


    def findWords(self, board: list[list[str]], words: list[str]) -> list:
        # Create a Trie using given words
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[self.WORDKEY] = word

        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board
        self.trie = trie
        self.matchedWords = []

        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] in self.trie:
                    self._dfs(row, col)

        return self.matchedWords



"""
Optimization: Pruning of the Trie i.e, Incrementally remove the matched leaf node in Trie !!
if not curNode:
    self.trie.pop(curNode)

"""


class Crossword3:
    def __init__(self) -> None:

        self.rows = None
        self.cols = None
        self.board = None
        self.trie = None
        self.matchedWords = None
        self.WORDKEY = "$"

    def _dfs(self, row: int, col: int) -> None:
        # Base Case --> Our Goal
        letter = self.board[row][col]
        curNode = self.trie[letter]
        if not curNode:
            self.trie.pop(letter)

        wordMatch = curNode.pop(self.WORDKEY, False)
        if wordMatch:
            self.matchedWords.append(wordMatch)

        # Mark the node as visited
        self.board[row][col] = "#"
        # Explore
        for rowOffset, colOffset in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            newRow, newCol = row + rowOffset, col + colOffset
            if newRow < 0 or newRow == self.rows or newCol < 0 or newCol == self.cols:
                continue
            self._dfs(newRow, newCol)

        # Undo --> Backtrack
        self.board[row][col] = letter

    def findWords(self, board: list[list[str]], words: list[str]) -> list:
        # Create a Trie using given words
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[self.WORDKEY] = word

        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board
        self.trie = trie
        self.matchedWords = []

        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] in self.trie:
                    self._dfs(row, col)

        return self.matchedWords