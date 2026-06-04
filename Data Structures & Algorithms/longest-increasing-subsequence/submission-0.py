class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_c = -1
        tracker = [-1]*len(nums)
        tracker[-1] = 0

        for i in range(len(nums)-1, -1, -1):
            n = nums[i]
            fil = []
            for j in range(i+1, len(nums)):
                if nums[j] > n:
                    fil.append(tracker[j])
            if fil:
                t_c = max(fil)
            else:
                t_c = -1
            
            tracker[i] = t_c + 1
            max_c = max(t_c+1, max_c)
        
        return max_c + 1