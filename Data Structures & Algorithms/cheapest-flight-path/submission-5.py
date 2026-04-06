class Solution:
    def pathHelper(self, source, k_stop, past, cost):
        print(f'\nsource:{source}, k_stop:{k_stop}, past: {past}, cost:{cost}')
        
        if cost > self.min_cost:
            return 
            
        if k_stop > self.k:
            return 
        else:
            past.append(source)

            if source == self.dst:
                print(f'Found dst at {k_stop} and cost: {cost}')
                self.min_cost = min(cost, self.min_cost)
                past.pop()
                return 
            
            for i in self.adjacency[source]:
                next_node, add_cost = i
                if next_node not in past:
                    print(f'Next node: {next_node}, cost:{add_cost}, updated_cost: {add_cost + cost}')
                    self.pathHelper(next_node, k_stop+1, past, cost+add_cost) 

            past.pop()


    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        self.adjacency = dict()
        self.dst = dst
        self.k = k+1
        self.min_cost = 1500

        for f in flights:
            source, destination, cost = f
            self.adjacency[source] = self.adjacency.get(source, []) + [[destination, cost]]
            self.adjacency[destination] = self.adjacency.get(destination, [])
    
        print('Adjacency: ', self.adjacency, end='\n\n')

        self.pathHelper(src, 0, [], 0)

        if self.min_cost == 1500:
            return -1
        else:
            return self.min_cost

        