import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # distance, x, y
        distance = [(x**2+y**2)**0.5 for (x,y) in points]
        combo = [[distance[i], points[i]] for i in range(len(distance))]

        heapq.heapify(combo)

        ret = []
        for i in range(k):
            _, coor = heapq.heappop(combo)
            ret.append(coor)
        
        return ret
