# A RouteTrie will store our routes and their associated handlers
from AutoComplete import TrieNode


class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.currentNode = self.root
        

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        """
        currentNode = self.root
        for word in path:
            if word not in currentNode.children.keys():
                currentNode.children[word] = RouteTrieNode()
            currentNode = currentNode.children[word]
        currentNode.handler = handler
        """
        for word in path:
            if word not in self.currentNode.children.keys():
                self.currentNode.children[word] = RouteTrieNode(handler)
            else:
                path = path[1:]
                self.currentNode = self.currentNode.children[word]
                self.currentNode.insert(path, handler)
        
       

    def find(self):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        pass

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = {}


    def insert(self, word, handler):
        # Insert the node as before
        self.children[word] = RouteTrieNode(handler)


route_trie = RouteTrie()

route_trie.insert(['about', 'me'], 'About handler')

print(route_trie.root.children)

route_trie.insert(['about', 'me'], 'Me handler')
print(route_trie.root.children)

import sys
TestText2 = route_trie.root.children.values()
# sys.stdout.buffer.write(TestText2)