class RouteTrieNode:
    def __init__(self, handler = None):
        self.handler = handler
        self.children = {}
   
    def insertNode(self, path):
        self.children[path] = RouteTrieNode()



class Trie:
    def __init__(self):
        self.root = RouteTrieNode()

    def insert(self, pathArray, handler):
        currentNode = self.root
        for path in pathArray:
            if path not in currentNode.children.keys():
                currentNode.insertNode(path)
            currentNode = currentNode.children[path]
        currentNode.handler = handler

    def find(self, pathArray):
        currentNode = self.root
        for path in pathArray:
            if path not in currentNode.children.keys():
                return None
            else:
                currentNode = currentNode.children[path]
        
        return currentNode.handler


class Router:
    def __init__(self):
        self.trie = Trie()

    def addHandler(self, url, handler):
        pathArray = url.split("/")
        if pathArray[-1] == "":
            pathArray.pop()
        self.trie.insert(pathArray,handler)

    def lookUp(self, url):
        if url == "/":
            return self.trie.root.handler
        pathArray = url.split("/")
        if pathArray[-1] == "":
            pathArray.pop()

        return self.trie.find(pathArray)

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one



