def check_board(board):
    for rec in board:
        tracker = [0]*10
        for ele in rec:
            if ele != ".":
                ele = int(ele)
                tracker[ele] += 1
                if tracker[ele] > 1:
                    return False
            
    return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        board_flip = [list(row) for row in zip(*board)]
        
        # check rows of board
        if not check_board(board):
            return False
        
        # check columns of board
        if not check_board(board_flip):
            return False
        
        # check boxes 
        boxes_mid = [
            [1,1], [1,4], [1, 7],
            [4,1], [4,4], [4, 7],
            [7,1], [7,4], [7, 7]
        ]
        box_coord = [
            [-1,-1], [-1, 0], [-1, +1],
            [0, -1], [0, 0], [0, +1],
            [+1, -1], [+1, 0], [+1, +1]
        ]
        for box in boxes_mid:
            list_ele = [0]*10
            x, y = box
            for bc in box_coord:
                x_op, y_op = bc
                x_new = x + x_op
                y_new = y + y_op
                ele = board[x_new][y_new]

                if ele != '.':
                    ele = int(ele)
                    list_ele[ele] += 1
                    if list_ele[ele] > 1:
                        return False
        
        return True



        




                



