
class Solution:
    def oceanHelper(self, coor, prev_h, past):
        curr_h = self.grid[coor[0]][coor[1]]

        if prev_h is None or prev_h >= curr_h:
            # safe to proceed
            # if self.memory[coor[0]][coor[1]] == 1:
            #     return 1
            
            # unexplored cell
            direction = [
                [-1, 0], [1, 0], [0, -1], [0, 1]
            ]

            pacific = False
            atlantic = False

            past.append(coor)

            for dr in direction:
                x, y = coor[0] + dr[0], coor[1] + dr[1]
                # print(x,y)
                if x == -1 and y >=0 and y < self.length:
                    pacific = True
                elif y == -1 and x >=0 and x < self.height:
                    pacific = True
                elif x == self.height and y >=0 and y < self.length:
                    atlantic = True
                elif y == self.length and x >= 0 and x < self.height:
                    atlantic = True
                elif x >= 0 and y >= 0 and x< self.height and y < self.length and (x,y) not in past:
                    # print(x,y)
                    res = self.oceanHelper((x,y), curr_h, past)
                    # if self.memory[x][y] == -1:
                    #     self.memory[x][y] = res
                    
                    if res == 1:
                        pacific = True
                        atlantic = True
                    elif res == 2:
                        pacific = True
                    elif res == 3:
                        atlantic = True
                    

            if pacific and atlantic:
                # if self.memory[coor[0]][coor[1]] != 1:
                #     self.memory[coor[0]][coor[1]] == 1
                self.cells.add(coor)
                return 1
            elif pacific and not atlantic:
                # self.memory[coor[0]][coor[1]] = 2
                return 2
            elif not pacific and atlantic:
                # self.memory[coor[0]][coor[1]] = 3
                return 3
            else:
                # self.memory[coor[0]][coor[1]] = 0
                return 0

        else:
            # cannot access
            return -1

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.grid = heights
        self.height = len(self.grid)
        self.length = len(self.grid[0])
        self.memory = [[-1]*self.length]*self.height

        self.cells = set()

        for i in range(self.height):
            for j in range(self.length):
                res = self.oceanHelper((i,j), None, [])
                if res == 1:
                    self.cells.add((i,j))
                    # self.memory[i][j] = 1
                # if self.memory[i][j] == -1:
                    # self.memory[i][j] = res
        
        list_cells = [list(i) for i in self.cells]
        # for k in self.grid:
        #     print(k)
        # print()
        # for k in self.memory:
        #     print(k)
        return list_cells