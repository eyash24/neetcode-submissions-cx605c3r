from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        min_num = min(nums[l], nums[r])
        # print('nums: ', nums)

        while l<=r:
            mid = (l+r)//2
            min_num = min(nums[mid], min_num, nums[l], nums[r])
            # print(f'l:{l}, r:{r}, mid:{mid}, mid_ele:{nums[mid]}')

            if nums[l] > nums[r]:
                if nums[mid] <= nums[r] and nums[mid] >= nums[l]:
                    r = mid -1
                elif nums[mid] >= nums[r] and nums[mid]>= nums[l]:
                    l = mid + 1
                elif nums[mid] <= nums[r] and nums[mid] <= nums[l]:
                    r = mid - 1
                elif nums[mid] >= nums[r] and nums[mid] <= nums[l]:
                    l = mid + 1
                else:
                    break
            else:
                if nums[mid] >= nums[r] and nums[mid]>= nums[l]:
                    r = mid -1
                elif nums[mid] <= nums[r] and nums[mid] <= nums[l]:\
                    l = mid +1 
                else:
                    break
            

        return min_num
            