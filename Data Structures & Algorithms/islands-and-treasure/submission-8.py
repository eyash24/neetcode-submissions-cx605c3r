class Solution:
    def islandHelper(self, coor, distance, past):
        print(min(distance,self.grid[coor[0]][coor[1]]))
        self.grid[coor[0]][coor[1]] = min(self.grid[coor[0]][coor[1]], distance)
        past.append(coor)
        direction = [
            [0, -1], [0, 1], [-1, 0], [1, 0]
        ]

        for dr in direction:
            x, y = coor[0] + dr[0], coor[1] + dr[1]

            if x >= 0 and x < self.height and y >= 0 and y < self.length and self.grid[x][y] not in [0, -1]:
                if ((x,y) in past and self.grid[x][y] > distance+1) or ((x,y) not in past):
                    self.islandHelper((x,y), distance+1, past)

        # past.pop()     


    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.grid = grid
        self.length = len(grid[0])
        self.height = len(grid)

        for i in range(self.height):
            for j in range(self.length):
                if self.grid[i][j] == 0:
                    print(i,j)
                    self.islandHelper((i,j), 0, [])

                    for k in self.grid:
                        print(k)
        
        grid = self.grid
                    
