class Solution:

    def islandHelper(self,coor, island):
        self.grid[coor[0]][coor[1]] = island
        self.count_cell += 1

        direction = [
            [0,-1], [0, 1], [1, 0], [-1, 0]
        ]

        for dr in direction:
            x = coor[0] + dr[0]
            y = coor[1] + dr[1]

            if x >= 0 and x < self.height and y >=0 and y < self.length and self.grid[x][y] == 1:
                self.islandHelper((x,y), island)



    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.length = len(grid[0])
        self.height = len(grid)
        self.max_area = 0
        no_island = 0

        for i in range(self.height):
            for j in range(self.length):
                if self.grid[i][j] == 1:
                    self.count_cell = 0
                    no_island = -1
                    self.islandHelper((i,j), no_island)
                    self.max_area = max(self.max_area, self.count_cell)
        
        return self.max_area
