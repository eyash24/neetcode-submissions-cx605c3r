class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        tracker = [-1]*(n+1)
        n_set = 0
        cycle = []

        for pr in edges:
            p1, p2 = pr
            
            if tracker[p1] == -1 and tracker[p2] == -1:
                tracker[p1] = tracker[p2] = n_set
                n_set += 1
            
            elif tracker[p1] == -1 and tracker[p2] > -1:
                tracker[p1] = tracker[p2]
            
            elif tracker[p1] > -1 and tracker[p2] == -1:
                tracker[p2] = tracker[p1]
            
            elif tracker[p1] > - 1 and tracker[p2] > -1 and tracker[p1]!=tracker[p2]:

                if tracker.count(tracker[p1]) > tracker.count(tracker[p2]):
                    old_p = tracker[p2]
                    new_p = tracker[p1]
                else:
                    old_p = tracker[p1]
                    new_p = tracker[p2]
                
                for p in range(1,n+1):
                    if tracker[p] == old_p:
                        tracker[p] = new_p
            
            elif tracker[p1] == tracker[p2]:
                cycle.append(pr)
        

        return cycle[-1]
