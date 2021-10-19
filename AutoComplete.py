# from ipywidgets import widgets
# from IPython.display import display
# from ipywidgets import interact

class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        # the keys are characters and the values are TrieNodes
        self.children = {}
        self.is_end_of_word = False
        ## Initialize this node in the Trie
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        # while self.is_end_of_word == False:
        if self.children == {}:
            return None
        # if self.letter:
        #     return self.letter
        # if self.is_end_of_word == True:
        currentChildren = self.children
        for letter, node in currentChildren.items():
            suffix += letter
            print(suffix)
            return node.suffixes
        
        return suffix
        
        
        
        
    
        
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

f("a")
# for child in MyTrie.root.children:
#     # print(MyTrie.find("fun"))
#     print(child)