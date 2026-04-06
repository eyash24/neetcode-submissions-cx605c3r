class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_length  = len(nums)
        if num_length <= 1:
            return num_length
        
        # For num_length >= 2
        # sort nums
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        
        seq_length = 1
        prev = nums[0]
        max_seq = 0

        for ele in nums[1:]:
            if prev == ele-1:
                seq_length += 1
                prev = ele
            else:
                max_seq = max(max_seq, seq_length)
                seq_length = 1
                prev = ele
        return max(max_seq, seq_length)
