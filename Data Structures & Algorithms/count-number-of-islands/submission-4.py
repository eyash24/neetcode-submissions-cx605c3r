class Solution:
    def islandHelper(self, coor, island):
        print('coord:', coor)
        self.grid[coor[0]][coor[1]] = island
        print(self.length, self.height)

        directions = [
            [0, -1], [0, 1], [-1, 0], [1, 0]
        ]

        for dr in directions:
            x = coor[0] + dr[0]
            y = coor[1] + dr[1]
            print('try: ',(x,y))

            if x >= 0 and x < self.length and y >= 0 and y < self.height and self.grid[x][y] == '1':
                # print('valid_coord: ', (x,y))
                # print('ele: ', self.grid[x][y])
                print('exploring coor: ', (x,y))
                self.islandHelper((x,y), island)
        

    def numIslands(self, grid: List[List[str]]) -> int:
        self.length = len(grid)
        self.height = len(grid[0])
        self.grid = grid
        no_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] == "1":
                    coor = (i,j)
                    no_island -= 1
                    self.islandHelper(coor,no_island)
        return -no_island
        
