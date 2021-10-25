I used a dictionary for the children property of the Trie Node to allow fast access when inserting or finding a specific Node of the trie.

In terms of time complexity it is O(n) since looking through the dictionary keys when inserting / finding takes O(n) time.  

In terms of space complexity it is O(n), since adding a new url / handler creates only one more node in the trie. 