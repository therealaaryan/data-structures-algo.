We will create a trieNode class with children(hashmap) and endOfWord(to signify if a node is the end of the word). We will then creatr a root as a constructor in the main class. We will navigate starting from that node. While inserting, we will see if the letter exists in children, if it doesn't then we will create a trieNode and default keep shifting to the children. For searching, just traverse through the trie tree.