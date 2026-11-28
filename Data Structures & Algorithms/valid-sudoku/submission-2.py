class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        square_coor = [
            [1,1], [1,4], [1,7],
            [4,1], [4,4], [4,7],
            [7,1], [7,4], [7,7]
        ]

        directions = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0,0], [0, 1],
            [1, -1], [1, 0], [1, 1]
        ]
        
        di_row_col = dict()
        for r_index in range(9):

            di_square = dict()
            di_row = dict()
            for c_index in range(9):
                val = board[r_index][c_index]

                if val != '.':
                    # row_check
                    di_row[val] = di_row.get(val, 0) + 1
                    if di_row[val] > 1:
                        return False

                    # col_check
                    di_row_col[c_index] = di_row_col.get(c_index, dict())
                    di_row_col[c_index][val] = di_row_col[c_index].get(val, 0) + 1
                    if di_row_col[c_index][val] > 1:
                        return False
                
                # square check 
                s_x, s_y = square_coor[r_index]
                c_x, c_y = directions[c_index]
                new_s_x, new_s_y = s_x + c_x, s_y + c_y
                s_val = board[new_s_x][new_s_y]

                if s_val != '.':
                    di_square[s_val] = di_square.get(s_val, 0) + 1
                    if di_square[s_val] > 1:
                        return False
        return True
                

            
         
                    

            
                



