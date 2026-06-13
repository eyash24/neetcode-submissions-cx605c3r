class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        track = [[i[1]-i[0]+1, i[0], i[1]] for i in intervals]
        track.sort()
        res = []

        for q in queries:
            flag = False
            min_sap = float('inf')

            for t in track:
                sap, s, e = t

                if s <= q <= e:
                    flag = True
                    min_sap = min(min_sap, sap)

            if flag:
                res.append(min_sap)
            else:
                res.append(-1) 
            
        return res




        
