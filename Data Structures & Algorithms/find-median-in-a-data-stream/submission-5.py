import heapq

class MedianFinder:

    def __init__(self):
        self.heap = []
        
    def addNum(self, num: int) -> None:
        self.heap.append(num)
        self.heap.sort()

    def findMedian(self) -> float:
        if len(self.heap)%2 == 0:
            # even
            y = int(len(self.heap)/2)
            return (self.heap[y] + self.heap[y-1])/ 2
        else:
            return self.heap[int(len(self.heap)/ 2)]
        