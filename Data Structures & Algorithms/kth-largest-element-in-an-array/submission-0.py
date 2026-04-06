import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-i for i in nums]
        heapq.heapify(max_heap)
        for i in range(k):
            pop_ret = heapq.heappop(max_heap)
        
        return pop_ret*(-1)
