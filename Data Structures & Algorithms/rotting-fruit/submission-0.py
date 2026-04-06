class Solution:

    def fruitHelper(self, coor, time, past):
        direction = [
            [0,-1], [0,1], [-1, 0], [1, 0]
        ]
        past.append(coor)

        if time < 0:
            if self.grid[coor[0]][coor[1]] == 1:
                self.grid[coor[0]][coor[1]] = time 
            else:
                self.grid[coor[0]][coor[1]] = max(self.grid[coor[0]][coor[1]], time)

        for dr in direction:
            x, y = coor[0] + dr[0], coor[1]+dr[1]
            if x >= 0 and x < self.height and y >= 0 and y < self.length and self.grid[x][y] not in [0,2]:
                if ((x, y) in past and time -1 > self.grid[x][y]) or ((x,y) not in past):
                    self.fruitHelper((x,y), time -1, past)

    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.length = len(grid[0])
        self.height = len(grid)

        for i in range(self.height):
            for j in range(self.length):
                if self.grid[i][j] == 2:
                    self.fruitHelper((i,j), 0, [])
        
        max_time = 0
        for i in range(self.height):
            for j in range(self.length):
                if self.grid[i][j] == 1:
                    return -1
                else:
                    max_time = max(max_time, -self.grid[i][j]) 
        
        return max_time
                    
        