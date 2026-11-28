class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        nums.sort()

        streak = 1
        max_streak = 1
        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                streak += 1
                max_streak = max(streak, max_streak)
            else:
                streak = 1
        
        return max_streak

