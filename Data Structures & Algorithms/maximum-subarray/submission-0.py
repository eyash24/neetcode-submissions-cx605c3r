class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        max_s = float('-inf')

        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                max_s = max(max_s, s)

        return max_s


        