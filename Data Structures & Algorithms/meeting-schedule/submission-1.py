"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        track = [[i.start,i.end] for i in intervals]
        if len(track) <= 1:
            return True
            
        track.sort()


        r = track[0][1]
        for i in range(1,len(track)):
            s, e = track[i]
            if s >= r:
                r = e
            else:
                return False
        else:
            return True

