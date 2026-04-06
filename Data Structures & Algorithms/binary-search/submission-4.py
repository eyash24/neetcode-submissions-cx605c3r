class Solution:
    def search(self, nums: List[int], target: int) -> int:
        limit = len(nums)
        r,l = 0, limit
        

        while r<=l:
            mid = (r+l)//2
            if mid < limit and nums[mid] == target:
                return mid
            elif mid < limit and nums[mid] < target:
                r = mid + 1
            else:
                l = mid - 1
        else:
            return -1
