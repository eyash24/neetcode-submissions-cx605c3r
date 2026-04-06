

class PrefixTree:

    def __init__(self):
        self.start = dict()
        

    def insert(self, word: str) -> None:
        self.start = self.insertHelper(self.start, word)
        
    def insertHelper(self, root, word):
        if word == '':
            root[None] = None
            return root

        ch = word[0]
        if len(word) > 1:
            word = word[1:]
        else:
            word = ''
        
        if ch in root:
            root[ch] = self.insertHelper(root[ch], word)
        else:
            root[ch] = self.insertHelper(dict(), word)
        
        return root

    def search(self, word: str) -> bool:
        return self.searchHelper(self.start, word)
    
    def searchHelper(self, root, word):
        if word == '':
            if None not in root:
                return False
            else:
                return True

        ch = word[0]
        word = word[1:] if len(word) > 1 else ''

        if ch in root:
            return True and self.searchHelper(root[ch], word)
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        return self.prefixHelper(self.start, prefix)

    def prefixHelper(self, root, word):
        if word == '':
            if root:
                return True
            else:
                return False

        ch = word[0]
        word = word[1:] if len(word) > 1 else ''

        if ch in root:
            return True and self.prefixHelper(root[ch], word)
        else:
            return False

        
        