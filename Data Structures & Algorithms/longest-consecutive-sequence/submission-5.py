class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        set_int = set()
        for n in nums:
            set_int.add(n)

        new_li = list(set_int)
        new_li.sort()

        if len(new_li) <= 1:
            return len(new_li)

        max_consecutive = 0

        limit = len(new_li)
        i = 0
        while i < limit:
            consecutive = 1
            while i+1 < limit and  new_li[i] + 1 == new_li[i+1]:
                consecutive += 1
                i += 1
                max_consecutive = max(consecutive, max_consecutive)
            i += 1
        
        return max_consecutive




        
