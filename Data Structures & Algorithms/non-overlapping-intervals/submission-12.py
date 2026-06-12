from typing import List

class Solution:
    def helper(self,i, r):
        if i >= self.n: return 0

        a = 1 + self.helper(i+1, r)
        b = float('inf')
        if self.intervals[i][0] >= r:
            b = self.helper(i+1, self.intervals[i][1])

        return min(a,b)

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <=1:
            return 0
        
        intervals.sort()
        self.intervals = intervals
        self.n = len(intervals)
        r = float('-inf')

        return self.helper(0, r)