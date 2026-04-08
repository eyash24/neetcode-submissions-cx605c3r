class Solution:
    def rob(self, nums: List[int]) -> int:
        limit = len(nums)
        if limit < 4:
            return max(nums)
        
        track = [[-1]*2 for _ in range(limit)]

        for i, c in enumerate(nums[:-2]):
            if i == 0:
                track[i][0] = c
                track[i][1] = 0
            
            elif i == 1:
                track[i][1] = c
                track[i][0] = 0
            
            print('pre: ', track)
            
            if i+2 < limit-1:
                if track[i+2][0] < track[i][0] + nums[i+2]:
                    track[i+2][0] = track[i][0] + nums[i+2]
            
            if i+2 <= limit-1 and track[i+2][1] < track[i][1] + nums[i+2]:
                track[i+2][1] = track[i][1] + nums[i+2]

            if i+3 < limit-1 and track[i+3][0] < track[i][0] + nums[i+3]:
                track[i+3][0] = track[i][0] + nums[i+3]
            
            if i+3 <= limit-1 and track[i+3][1] < track[i][1] + nums[i+3]:
                track[i+3][1] = track[i][1] + nums[i+3]

            print(track)
        
        vals = [max(i) for i in track]
        return max(vals)

                
                                
                


