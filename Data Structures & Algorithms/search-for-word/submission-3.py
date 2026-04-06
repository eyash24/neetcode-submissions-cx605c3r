class Solution:
    def wordHelper(self, index, i,j, past):
        print('index: ', i)
        print('current coor: ', i, j)
        print('past: ', past)
        print(self.word[index])
        past.append([i,j])
        if self.word[index] == self.board[i][j] and index +1 == len(self.word):
            return True
        
        elif self.word[index] == self.board[i][j]:
            for d in self.direction:
                next_i = i+d[0]
                next_j = j+d[1]
                print('new coor: ',next_i, next_j)
                if next_i >= 0 and next_i < self.v_high and next_j >= 0 and next_j < self.h_high and [next_i, next_j] not in past:
                    if self.wordHelper(index+1, next_i, next_j, past):
                        print(past)
                        return True
            past.pop()
            return False

        else:
            past.pop()
            return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.v_high = len(board)
        self.h_high = len(board[0])
        self.direction = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        self.word = word
        self.res = False

        for i in range(self.v_high):
            for j in range(self.h_high):
                if self.wordHelper(0, i, j, []):
                    return True
        else:
            return False



        