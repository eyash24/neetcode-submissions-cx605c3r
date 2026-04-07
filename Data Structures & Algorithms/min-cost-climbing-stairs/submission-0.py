class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        limit = len(cost) + 1
        track = [-1]*limit
        track[0] = 0
        
        for i, c in enumerate(cost):
            if i == 1 or i == 0:
                c_update = c
            else:
                c_update = track[i]+c
                
            if i+1 < limit and track[i+1] < 0:
                if i+1 == 1:
                    track[i+1] = min(cost[i+1], c_update)
                else:
                    track[i+1] = c_update
            elif i+1 < limit and track[i+1] > -1:
                track[i+1] = min(track[i+1], c_update)

            if i+2 < limit and track[i+2] < 0:
                track[i+2] = c_update
            elif i+2 < limit and track[i+2] > -1:
                track[i+2] = min(track[i+2], c_update)
            print(track)
            print()
        # print(track)
        return track[-1]
            
