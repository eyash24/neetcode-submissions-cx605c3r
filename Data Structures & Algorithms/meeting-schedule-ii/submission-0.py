"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        tracks = [[i.start, i.end] for i in intervals]
        
        if len(tracks) < 1:
            return 0

        tracks.sort()

        ends = [tracks[0][1]]

        for t in range(1,len(tracks)):
            s1, e1 = tracks[t]

            for j in range(len(ends)):
                r = ends[j]
                if s1 >= ends[j]:
                    ends[j] = e1
                    break
            else:
                ends.append(e1)
                ends.sort()

        return len(ends)


