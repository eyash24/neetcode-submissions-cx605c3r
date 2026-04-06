import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.max_heap = [-i for i in nums]
        heapq.heapify(self.max_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.max_heap, -val)
        ret_val = []
        for i in range(self.k):
            pop_val = heapq.heappop(self.max_heap)
            ret_val.append(pop_val)
        
        for i in range(self.k):
            heapq.heappush(self.max_heap,ret_val[i])
        
        return pop_val*(-1)

        
