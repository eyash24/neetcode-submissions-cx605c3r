class WordDictionary:

    def __init__(self):
        self.start = dict()
        

    def addWord(self, word: str) -> None:
        print('Operation: Add Word: ', word)
        self.start = self.addHelper(self.start, word)
        print(self.start)

    def addHelper(self, root, word):
        if word == '':
            root[None] = None
            return root

        ch = word[0]
        word = word[1:] if len(word) > 1 else ''
        
        if ch in root:
            root[ch] = self.addHelper(root[ch], word)
        else:
            root[ch] = self.addHelper(dict(), word)
        
        return root
        
    
    def search(self, word: str) -> bool:
        return self.searchHelper(self.start, word)

    
    def searchHelper(self, root, word):
        if word == '':
            if None in root.keys():
                return True
            else:
                return False 

        ch = word[0]
        word = word[1:] if len(word) > 0 else ''
        
        if ch != '.':
            if root is None:
                return False

            if ch in root:
                return True and self.searchHelper(root[ch], word)
            else:
                return False
        else:
            if root is None:
                return False

            if len(word) == 0:
                # last ch == '.'
                keys = list(root.keys())
                if None in keys:
                    keys.remove(None)
                
                if len(keys) > 0:
                    for k in keys:
                        if self.searchHelper(root[k], '') is True:
                            return True
                    else:
                        return False
                else:
                    return False 

            else:
                # not last character
                keys = list(root.keys())
                if None in keys:
                    keys.remove(None)
                
                for k in keys:
                    if self.searchHelper(root[k], word) is True:
                        return True
                else:
                    return False
                

        
        
        


        
