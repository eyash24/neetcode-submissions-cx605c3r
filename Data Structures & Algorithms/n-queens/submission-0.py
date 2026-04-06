def check_coor(coor, past, n):
    h_limit = n-1
    if past == []:
        return True
    else:
        i_level, i = coor # to check

        for cr in past:
            j_level, j = cr # past coor
            if j == i:
                return False
            
            diagonal_coor = [
                (i_level, j+(i_level - j_level)),
                (i_level, j - (i_level - j_level))
            ]
            print(diagonal_coor)

            for dc in diagonal_coor:
                if dc[1] >= 0 and dc[1] <= h_limit:
                    if coor == dc:
                        return False

        return True
            

class Solution:
    def queenHelper(self, n, level, past):
        if level+1 < n:
            for i in range(n):
                coor = (level, i)
                if check_coor(coor, past, n):
                    new_past = past + [coor]
                    self.queenHelper(n, level+1,new_past)
        else:
            for i in range(n):
                coor = (level, i)
                if check_coor(coor, past, n):
                    new_past = past + [coor]
                    self.sol.append(new_past.copy())
        

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.sol = []
        self.queenHelper(n, 0, [])

        print(self.sol)
        boards = []
        for l in self.sol:
            board = []
            for coor in l:
                _, j = coor
                row = '.'*j+'Q'+'.'*(n-j-1)
                board.append(row)
            boards.append(board)
        
        return boards
        
                

