class Solution:
    def __init__(self):
        self.start = {'ignore':[]}
        self.wordsFound = set()

    def addwordHelper(self, root, word, building):
        if word == '':
            root[None] = building
            return root

        ch = word[0]
        word = word[1:] if len(word)>1 else ''

        if ch in root:
            root[ch] = self.addwordHelper(root[ch], word, building)
        else:
            new_dict = {'ignore':[]}
            root[ch] = self.addwordHelper(new_dict, word, building)
        
        return root
    
    def findHelper(self, coor, root, past):
        # print(f'coor:{coor}, root:{root}, past:{past}, word:{word}')

        x,y = coor
        ch = self.board[x][y]
        keys = list(root.keys())
        if ch in root['ignore']:
            return False

        if None in root:
            self.wordsFound.add(root[None])

            if len(root) <= 1:
                return False

        next_past = past.copy()
        next_past.add(str([x,y]))

        if ch in root:

            valid = False
            # if direction exist
            for direc in self.directions:
                new_x = x + direc[0] # i
                new_y = y + direc[1] # j
                # print('new coor helper: ', new_x, new_y)
                if new_x >= self.i_low and new_x <= self.i_high and new_y >= self.j_low and new_y <= self.j_high and str([new_x, new_y]) not in past:
                    valid = True
                    res = self.findHelper(
                        coor=[new_x, new_y], 
                        root=root[ch], 
                        past=next_past
                    )

                    if res is False:
                        root['ignore'].append(ch)

            if not valid:
                # print('found no next coor')
                if None in root[ch]:
                    inner_root = root[ch]
                    self.wordsFound.add(inner_root[None])
                    if len(inner_root) > 1:
                        return True
                    else:
                        return False
        return True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # create word dictionary
        self.board = board
        for w in words:
            self.start = self.addwordHelper(self.start, w, w)
        
        print(self.start)
        
        self.i_low, self.i_high = 0, len(board)-1
        j_row = board[0]
        self.j_low, self.j_high = 0, len(j_row)-1

        self.directions = [[-1,0], [0,-1], [0,1], [1,0]]

        for i in range(0, self.i_high+1):
            for j in range(0, self.j_high+1):
                ch = self.board[i][j]
                # print('searching for ch: ', ch)
                if ch in self.start:
                    # print(f'ch: {ch} exist in start')
                    if None in self.start[ch] and ch not in self.wordsFound:
                        inner_root = self.start[ch]
                        self.wordsFound.add(inner_root[None])

                        if len(inner_root) <=1:
                            self.start['ignore'].append(ch)


                    for direc in self.directions:
                        new_x = i + direc[0] # i
                        new_y = j + direc[1] # j
                        # print('new coor: ', new_x, new_y)
                        if new_x >= self.i_low and new_x <= self.i_high and new_y >= self.j_low and new_y <= self.j_high:
                            # print(f'Valid coor: [{new_x, new_y}]')
                            # print('\npast:',i,j)
                            past = set()
                            past.add(str([i,j]))
                            res = self.findHelper(
                                coor=[new_x, new_y],
                                root=self.start[ch], 
                                past=past
                            )
                            if res is False:
                                root['ignore'].append(ch)
                        # else:
                        #     print('coor not selected')
        
        return list(self.wordsFound)

        
        

        