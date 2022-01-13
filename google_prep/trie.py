class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    # O(n)
    def insert(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()
            curr = curr.children[char]
        curr.isWord = True

    # O(n)
    def search(self, word):
        curr = self
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            if curr.isWord:
                return True
        return False
        
    # O(n)
    def startsWith(self, prefix):
        curr = self
        for char in prefix:
            if char in self.children:
                curr = curr.children[char]
            else:
                return False
        return True