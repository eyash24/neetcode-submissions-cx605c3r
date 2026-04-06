from collections import defaultdict
import heapq

class Solution:

    def pathHelper(self, node):
        while self.graph[node]:
            next_node = heapq.heappop(self.graph[node])
            self.pathHelper(next_node)
        self.path.append(node)


    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.graph = defaultdict(list)
        self.path = []

        for t in tickets:
            heapq.heappush(self.graph[t[0]], t[1])
        
        print(self.graph)

        self.pathHelper('JFK')

        return self.path[::-1]

        