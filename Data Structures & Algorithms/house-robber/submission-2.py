class Solution:
    def rob(self, nums: List[int]) -> int:
        limit = len(nums)
        if limit < 2:
            return nums[-1]
        
        track = [-1]*limit
        track[0], track[1] = nums[0], nums[1]
        # max_track = 0

        for i, c in enumerate(nums[:-2]):
            if track[i] == -1:
                c_update = c
                track[i] = c
            else:
                c_update = track[i]
            
            if i+2 < limit and nums[i+2] < -1:
                track[i+2] = c_update + nums[i+2]

            elif i+2 < limit and nums[i+2] > -1:
                track[i+2] = max(c_update+nums[i+2], track[i+2])


            if i+3 < limit and nums[i+3] < -1:
                track[i+3] = c_update + nums[i+3]
            elif i+3 < limit and nums[i+3] > -1:
                track[i+3] = max(c_update + nums[i+3], track[i+3])
            
            print(track)
        
        return max(track)
        


