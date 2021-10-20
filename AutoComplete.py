# from ipywidgets import widgets
# from IPython.display import display
# from ipywidgets import interact

class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.auxArray = []
        self.children = {}
        self.is_end_of_word = False

    def suffixes(self, suffix = ''):
        currentChildren = self.children
        if self.is_end_of_word == True:
            self.auxArray.append(suffix)
            # print(self.auxArray)
        for letter, node in currentChildren.items():
            suffix += letter
            print(suffix)
            # currentBranch = node.suffixes(suffix)
            self.auxArray += node.suffixes(suffix)
            suffix = suffix[:-1] 
        # print(self.auxArray)
        return self.auxArray
        
        
        
        
    
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode("*")

    def insert(self, word):
        ## Add a word to the Trie
        currentNode = self.root
        if word == "":
            return 
        for char in word:
            if char not in currentNode.children.keys():
                currentNode.children[char] = TrieNode(char)
            currentNode = currentNode.children[char]
        currentNode.is_end_of_word = True
    
    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        currentNode = self.root
        if prefix == "":
            return currentNode
        for char in prefix:
            if char not in currentNode.children.keys():
                return None
            else:
               currentNode = currentNode.children[char]

        return currentNode

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            # print('\n'.join(prefixNode.suffixes()))
            print(prefixNode.suffixes())
        else:
            print(prefix + " not found")
    else:
        print('')

f("tr")
# for child in MyTrie.root.children:
#     # print(MyTrie.find("fun"))
#     print(child)