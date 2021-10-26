I used a Trie with a dictionary for the children property of the Trie Node to allow fast access when inserting or finding a specific Node of the trie.

In terms of time complexity it is O(n) since looking through the dictionary keys when inserting / finding takes O(n) time.  

In terms of space complexity it is O(n) because each letter of the word is stored in the trie. 