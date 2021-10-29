I used a Trie with a dictionary for the children property of the Trie Node to allow fast access when inserting or finding a specific Node of the trie.

For class TrieNode, the method suffixes is O(n) in terms of time complexity because for that node, there may be more than one child.  The space complexity is O(n) because
new memory is allocated for the suffixes that are found while traversing the Trie.  

For the find and insert methods of class Trie, the time complexity is O(n) since looking through the dictionary keys when inserting / finding takes O(n) time.  
In terms of space complexity it is O(n) because each letter of the word is stored in the trie -- the worst case scenario is that none of the letters in the word we want to insert exist in the same order, meaning new memory must be created for each letter as a node in the Trie.