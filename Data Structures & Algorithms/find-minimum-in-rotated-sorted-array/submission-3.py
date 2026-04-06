class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        n=len(nums)
        high = n-1
        min_ele = nums[0]        

        while low <= high:
            mid = low + (high-low) // 2
            min_ele = min(min_ele, nums[mid])

            if nums[mid] < nums[high]:
                high = mid -1
            else:
                low = mid + 1
        
        return min_ele

            