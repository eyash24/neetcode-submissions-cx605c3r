class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        track = []

        ele_limits = dict()

        for i in range(len(s)):
            if s[i] not in ele_limits:
                ele_limits[s[i]] = [i, i]
            else:
                start, limit = ele_limits.get(s[i])
                limit = max(limit, i)
                ele_limits[s[i]] = [start, limit]

        # print('ele_limts: ', ele_limits)

        i = 0
        while i < len(s):
            print('i: ', i)
            ele = s[i]
            start, limit = ele_limits[ele]
            
            j = i
            while j < limit+1:
                limit = max(limit, ele_limits[s[j]][1])
                j+=1
            track.append(j-i)
            i = j
        
        return track




        