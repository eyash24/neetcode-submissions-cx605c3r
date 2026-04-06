from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        n_set = 0
        set_tracker = [-1]*n

        for pr in edges:
            p1, p2 = pr
            print(pr)

            if p1 == p2:
                return False

            if set_tracker[p1] == -1 and set_tracker[p2] == -1:
                set_tracker[p1] = set_tracker[p2] = n_set
                n_set += 1
            
            elif set_tracker[p1] > -1 and set_tracker[p2] == -1:
                set_tracker[p2] = set_tracker[p1]
            
            elif set_tracker[p1] == -1 and set_tracker[p2] > -1:
                set_tracker[p1] = set_tracker[p2]
            
            elif set_tracker[p1] > -1 and set_tracker[p2] > -1:
                if set_tracker[p1] == set_tracker[p2]:
                    # cycle
                    return False
                
                else:
                    set_p1 = set_tracker.count(set_tracker[p1])
                    set_p2 = set_tracker.count(set_tracker[p2])

                    if set_p1 > set_p2:
                        combine_set = set_tracker[p1]
                        old_p = set_tracker[p2]
                    else:
                        old_p = set_tracker[p1]
                        combine_set = set_tracker[p2]
                    
                    for i in range(n):
                        if set_tracker[i] == old_p:
                            set_tracker[i] = combine_set

            print(set_tracker)


        if len(set(set_tracker)) > 1:
            return False
        return True