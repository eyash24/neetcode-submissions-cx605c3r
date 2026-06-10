class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l_intervals = len(intervals)

        if l_intervals <= 1:
            return intervals 
        
        s, e = intervals[0]
        i = 0

        res = intervals[0:1]

        for i in range(1, l_intervals):
            s1, e1 = res.pop()
            s2, e2 = intervals[i]

            if s1 == s2:
                s1, e1 = s1, max(e1, e2)
                res.append([s1, e1])
            elif s2 > s1 and e2 <= e1:
                res.append([s1, e1])
            elif s2 > e1:
                res.extend([[s1, e1], [s2, e2]])
            elif s2 <= e1:
                res.append([s1, e2])

        
        return res


