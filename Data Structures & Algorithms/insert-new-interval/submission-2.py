from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l_intervals = len(intervals)
        if l_intervals == 0:
            return [newInterval]
        
        s, e = newInterval
        
        s_i, e_i = 0, 0
        while s_i < l_intervals:
            if s > intervals[s_i][0]  and s > intervals[s_i][1]:
                s_i += 1
            
            elif s == intervals[s_i][0] or s == intervals[s_i][1]:
                print(f'found s_i: {s_i}')
                break
                
            elif s >= intervals[s_i][0] and s <= intervals[s_i][1]:
                break

            elif s < intervals[s_i][0]:
                s_i -= 1
                print(f'found s_i: {s_i}')
                break

        while e_i < l_intervals:
            print(f'e_i: {e_i}')
            if e > intervals[e_i][1] :
                e_i += 1
            
            elif e == intervals[e_i][1] or e == intervals[e_i][0]:
                print(f'found e_i: {e_i}')
                break
            
            elif e <= intervals[e_i][1] and e >= intervals[e_i][0]:
                print(f'found e_i: {e_i}')
                break
            
            elif e < intervals[e_i][0]:
                e_i -= 1
                print(f'found e_i:{e_i}')
                break

        print(f"s_i: {s_i}, e_i: {e_i}")

        if s_i == e_i and s_i == l_intervals:
            # last ele
            return intervals + [[s,e]]

        elif s_i == e_i:
            if s > intervals[s_i][1]:
                # new ele
                res = intervals[:s_i]
                res.append(intervals[s_i])
                res.append([s,e])
                if s_i +1 < l_intervals:
                    res.extend(intervals[s_i+1: ])
                return res
            
            else:
                if s_i >= 0:
                    res = intervals[:s_i]
                    
                    res.append([min(s, intervals[s_i][0]), max(e, intervals[e_i][1])])
                    if s_i + 1 < l_intervals:
                        res.extend(intervals[s_i+1:])
                    return res 
                else:
                    res = [[s,e]]
                    res.extend(intervals)
                    return res 
                
        elif s_i != e_i:
            if s_i >= 0 and e_i >= 0 and s_i < l_intervals and e_i < l_intervals:
                res = intervals[:s_i]
                if s > intervals[s_i][1]:
                    res.append(intervals[s_i])
                    if e_i < l_intervals:
                        res.append([s, max(intervals[e_i][1])])
                    else:
                        res.append([s, e])
                    
                else:
                    res.append([min(s, intervals[s_i][0]), max(e, intervals[e_i][1])])
                    
                if e_i +1 < l_intervals:
                    res.extend(intervals[e_i+1:])
                return res 

            elif s_i < 0:
                if e_i == l_intervals:
                    return [[s, e]]
                else:
                    res = [[s, max(intervals[e_i][1], e)]]
                    if e_i + 1 < l_intervals:
                        res.extend(intervals[e_i+1:])
                    return res
                
            elif e_i == l_intervals and s_i >= 0:
                res = intervals[:s_i]
                if s > intervals[s_i][1]:
                    res.append(intervals[s_i])
                    res.append([s, e])
                else:
                    res.append([min(s, intervals[s_i][0]), e])
                
                return res 
                