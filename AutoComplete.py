class TrieNode:
    def __init__(self):
        self.letter = ""
        # the keys are characters and the values are TrieNodes
        self.children = {}
        self.is_end_of_word = False
        ## Initialize this node in the Trie
    
    def insert(self, char):
        ## Add a child node in this Trie
        if self.letter == "":
            self.letter = char
        # add char 
        self.children[char] = TrieNode()
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)

    def insert(self, word):
        ## Add a word to the Trie

    def find(self, prefix):
        ## Find the Trie node that represents this prefix

