from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        tracker = [-1]*n
        n_set = 0
        
        for pr in edges:
            p1, p2 = pr
            # print(pr)

            if p1 == p2:
                continue
            
            if tracker[p1] == -1 and tracker[p2] == -1:
                tracker[p1] = tracker[p2] = n_set
                n_set += 1
            
            elif tracker[p1] == -1 and tracker[p2] > -1:
                tracker[p1] = tracker[p2]
            
            elif tracker[p1] > -1 and tracker[p2] == -1:
                tracker[p2] = tracker[p1]
            
            else:

                if tracker.count(tracker[p1]) > tracker.count(tracker[p2]):
                    old_p = tracker[p2]
                    new_p = tracker[p1]
                else:
                    old_p = tracker[p1]
                    new_p = tracker[p2]
                
                for p in range(n):
                    if tracker[p] == old_p:
                        tracker[p] = new_p
            # print(tracker)

        if -1 not in set(tracker):
            return len(set(tracker))
        else:
            add = tracker.count(-1)
            return len(set(tracker)) + add -1

       