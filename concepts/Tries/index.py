class TrieNode:
    def __init__(self, value = None):
        self.val = value
        self.neighbor = {_: None for _ in "abcdefghijklmnopqrstuvwxyz"}
        self.is_end = False
        
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
        
    def addWord(self, word):
        pointer = self.root
        
        while word != "":
            firstLetter = word[0]
            if pointer.neighbor[firstLetter] is None:
                pointer.neighbor[firstLetter] = TrieNode(firstLetter)
                pointer = pointer.neighbor[firstLetter]
            else:
                pointer = pointer.neighbor[firstLetter]
                
            word = word[1:]
        pointer.is_end = True
    
    def __recursivePrint(self, node, wordSoFar):
        wordSoFar += node.val
        if node.is_end:
            print(wordSoFar)
            return
        
        for neighbor in node.neighbor:
            if node.neighbor[neighbor] is not None:
                self.__recursivePrint(node.neighbor[neighbor], wordSoFar)
        return 
    
    def printTrie(self):
        for neighbor in self.root.neighbor:
            if self.root.neighbor[neighbor] is not None:
                self.__recursivePrint(self.root.neighbor[neighbor], "")
    
    def findPrefix(self, prefix):
        pointer = self.root
        while prefix != "":
            firstLetter = prefix[0]
            if pointer.neighbor[firstLetter] is None:
                return False
            pointer = pointer.neighbor[firstLetter]
            prefix = prefix[1:]
            
        return True
        
        

trie = Trie()
trie.addWord("hello")
trie.addWord("helpo")
trie.addWord("arpit")
trie.addWord("arijit")
trie.addWord("arijita")
trie.printTrie()
trie.printTrie()
print(trie.findPrefix("hel"))
print(trie.findPrefix("help"))
print(trie.findPrefix("heo"))