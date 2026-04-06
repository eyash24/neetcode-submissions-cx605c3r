class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        tracker = [-1]*(n+1)
        neighbors_dict = dict()
        
        for e in times:
            p1, p2, t = e
            neighbors_dict[p1] = neighbors_dict.get(p1, []) + [(p2, t)]
        
        queue = [(k, 0)]

        print('neighbors_dict: ',neighbors_dict)

        while queue:
            node, t = queue.pop(0)
            if tracker[node] == -1 or tracker[node] > t:
                tracker[node] = t

                neighbors = neighbors_dict.get(node, [])

                if len(neighbors)> 0:
                    for ngh in neighbors:
                        node, transmit_time = ngh
                        queue.append((node, t+transmit_time))

        print('tracker: ', tracker)
        if -1 in tracker[1:]:
            return -1
        else:
            return max(tracker)

                

                        

            
        


        