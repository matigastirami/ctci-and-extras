class TrieNode:
    def __init__(self):
        self.children = [None] * 26 # This array will represent the entire alphabet
        self.is_leaf = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        current = self.root
        for letter in word:
            # Get the position of the letter in the dictionary by subtracting the ascii value of 'a' to the ascii of letter
            index = ord(letter) - ord('a')
            if not current.children[index]:
                current.children[index] = TrieNode()
            current = current.children[index]
            current.is_leaf = True