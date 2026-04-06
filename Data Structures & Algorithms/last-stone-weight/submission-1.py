import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.max_heap = [-i for i in stones]
        heapq.heapify(self.max_heap)
        
        while len(self.max_heap) > 1:
            x = heapq.heappop(self.max_heap)*-1
            y = heapq.heappop(self.max_heap)*-1
            print(x, y)
            if x-y == 0:
                continue
            else:
                heapq.heappush(self.max_heap, (x-y)*-1)
        
        if len(self.max_heap) == 1:
            return self.max_heap[0]*-1
        else:
            return 0