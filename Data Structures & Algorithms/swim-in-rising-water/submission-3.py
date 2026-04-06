import heapq
from typing import List
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        queue = []
        height_limit = len(grid)
        width_limit = len(grid[0])
        graph = [[-1]*width_limit for i in range(height_limit)]


        heapq.heappush(queue, (0, (0,0)))
        direction = [
            [0,-1], [0, 1], [1, 0], [-1, 0]
        ]

        while queue:
            t, coor = heapq.heappop(queue)
            # print(f'\nt: {t}, coor:{coor}, graph val: {graph[coor[0]][coor[1]]}, grid val: {grid[coor[0]][coor[1]]}')
            # print('Grid: ')
            # for r in grid:
                # print(r)

            # print('\nGraph: ')
            # for r in graph:
                # print(r)

            add_queue = False
            # print()
            if graph[coor[0]][coor[1]] == -1:
                # print('Graph val is -1')
                if t >= grid[coor[0]][coor[1]]:
                    # print('t >= grid val, setting graph val = t')
                    graph[coor[0]][coor[1]] = t
                    # print('Updated graph:')
                    # for r in graph:
                        # print(r)
                    
                else:
                    # print('t < grid val, setting graph val = grid val')
                    graph[coor[0]][coor[1]] = grid[coor[0]][coor[1]]
                    # print('Updated graph:')
                    # for r in graph:
                        # print(r)

                add_queue = True

            else:
                # print('grid val not -1')
                if t < graph[coor[0]][coor[1]] and t >= grid[coor[0]][coor[1]]:
                    # print('t < graph val and t >= grid val, setting graph val = t')
                    graph[coor[0]][coor[1]] = t
                    add_queue = True

            if add_queue:
                new_t = graph[coor[0]][coor[1]]

                for d in direction:
                    x = coor[0] + d[0]
                    y = coor[1] + d[1]

                    if x >= 0 and x < height_limit and y >= 0 and y < width_limit:
                        heapq.heappush(queue,(new_t, (x,y)))
                
            # print('Updated graph: ')
            # for r in graph:
            #     print(r)

            
        return graph[height_limit-1][width_limit-1]