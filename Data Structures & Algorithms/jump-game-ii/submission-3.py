class Solution:
    def jump(self, nums: List[int]) -> int:
        l,r = 0, 0
        limit = len(nums)
        steps = 0

        while r < limit-1 and l < limit:
            # print(f'limit,  l, r: {limit, l, r}')
            max_j = 0
            for i in range(l, r+1):
                j = nums[i]
                if j > max_j and i + j > r:
                    max_j = j

            l += 1
            r = r + max_j
            if max_j > 0:
                steps += 1
        
        return steps