"""
Problem : Name search suggestions in mobile (Trie).
At every node of the Trie we will have 26 branches.
Trie Node
    - isNone: bool
    - child: [TrieNode]
    - frequency: int
    - topTen: list[str]

To make the things Memory Efficient, rather than empty lists for various letters,
then we can have childHash.
childHash :: key --> any letter a-z
             value --> nextChild

Go for post-processing and store the words in the list and sorted too if we have such requirements.

"""

class Trie:  # Implementation
    def __init__(self):
        """ Initialize data structure """
        self.root = {"isWord": False}

    def insert(self, word: str) -> None:
        """ Insert a word into Trie """
        cur = self.root
        for char in word:
            if char not in cur:
                cur[char] = {"isWord": False}
            cur = cur[char]
        cur["isWord"] = True

    def search(self, word: str) -> bool:
        """ Return True if the word is in Trie else False """
        cur = self.root
        for char in word:
            if char not in cur:
                return False
            cur = cur[char]
        return cur["isWord"]

    def startsWith(self, prefix: str) -> bool:
        """ Return True if there is any word in the Trie that starts with the given string else False"""
        cur = self.root
        for char in prefix:
            if char not in cur:
                return False
            cur = cur[char]
        return True

"""
Problem : Replace words with Prefix

Approach 1: Using HashMap
        TC: O(N*L)
        SC: O(N)
        
Approach 2: Using Trie
"""


class TrieSolution:
    def __init__(self) -> None:
        self.root = {}

    def insert(self, word) -> None:
        cur = self.root
        for char in word:
            cur = cur.setdefault(char, {})
        cur["isWord"] = word

    def replace(self, word):
        cur = self.root
        for char in word:
            cur = cur.get(char)
            if not cur:
                return word  # Not in the Trie
            if "isWord" in cur:
                return cur["isWord"]  # Shortest prefix
        return word


class Solution:
    @staticmethod
    def replaceWordsWithPrefixUsingHashMap(prefixes: list[str], sentence: str) -> str:
        words = sentence.split(" ")
        N = len(words)
        # Create a HashMap of prefixes
        prefixMap = {prefix: True for prefix in prefixes}

        for idx in range(N):
            word = words[idx]
            for letterIdx in word:
                if word[:letterIdx] in prefixMap:
                    words[idx] = prefixMap[word[:letterIdx]]
                    break

        return " ".join(words)

    @staticmethod
    def replaceWordsWithPrefixUsingTrie(dictionary: list[str], sentence: str) -> str:
        trie = TrieSolution()
        for word in dictionary:
            trie.insert(word)
        words = sentence.split(" ")
        return " ". join(trie.replace(word) for word in words)
