class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        box_centre_coor = [
            [1,1], [1,4], [1,7],
            [4,1], [4,4], [4,7],
            [7,1], [7,4], [7,7]   
        ]
        box_edges_coor = [
            [-1,-1], [-1,0], [-1,+1],
            [0,-1], [0,+1],
            [+1,-1], [+1,0], [+1,+1]
        ]

        columns = [[]]*9

        dupli_dict = {}
        
        # checking rows
        for row in board:
            col = 0
            for ele in row:
                if ele == ".":
                    col += 1
                    continue
                columns[col] = columns[col] + [ele]
                col += 1
                if ele not in dupli_dict.keys():
                    dupli_dict[ele] = 1
                else:
                    # print("case 1: ", row, ele)
                    return False
            dupli_dict.clear()
        
        dupli_dict.clear()
        # checking cols
        for cl in columns:
            for ele in cl:
                if ele == ".":
                    continue 
                if ele not in dupli_dict.keys():
                    dupli_dict[ele] = 1
                else:
                    # print("case 2: ", columns, ele)
                    return False
            dupli_dict.clear()
        
        # checking the boxes:
        dupli_dict.clear()
        for centre in box_centre_coor:
            i,j = centre[0], centre[1]
            dupli_dict[board[i][j]] = 1

            for edge in box_edges_coor:
                new_i = i + edge[0]
                new_j = j + edge[1]

                ele = board[new_i][new_j]
                if ele == ".":
                    continue

                if ele not in dupli_dict.keys():
                    dupli_dict[ele] = 1
                else:
                    # print("case 3: ",ele, centre,dupli_dict)
                    return False
            dupli_dict.clear()

        return True