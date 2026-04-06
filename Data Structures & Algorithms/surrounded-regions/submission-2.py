class Solution:
    def regionHelper(self,coor, past):
        # print('Evaluating coor: ', coor)

        if self.grid[coor[0]][coor[1]] == 'X':
            return True
        else:
            past.append(coor)

            direction = [
                [0, -1], [0, 1], [1, 0], [-1, 0]
            ]

            res_list = []
            for dr in direction:
                x, y = coor[0] + dr[0], coor[1]+dr[1]
                # print(x,y)
                if x >=0 and y >=0 and x < self.height and y < self.length and (x, y) not in past:
                    # print(f'exploring: {x,y}')
                    res_list.append(self.regionHelper((x, y), past))
                elif x <0 or x >= self.height or y < 0 or y >= self.length:
                    # print('False')
                    res_list.append(False)

            # print(f'For coor: {coor}, res_list:{res_list}')
            for r in res_list:
                if r == False:
                    return False

            return True
        

    def solve(self, board: List[List[str]]):
        self.grid = board
        self.length = len(self.grid[0])
        self.height = len(self.grid)

        for i in range(self.height):
            for j in range(self.length):
                if self.grid[i][j] == 'O':
                    if self.regionHelper((i,j), []):
                        self.grid[i][j] = 'X'
                # print()
                # for k in self.grid:
                #     print(k)
                # print()
        board = self.grid
        # return self.grid