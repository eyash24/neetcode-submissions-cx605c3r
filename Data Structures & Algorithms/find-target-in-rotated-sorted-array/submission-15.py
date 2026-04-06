from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        print('nums:', nums, ' target: ', target)

        while l <= r:
            m = (l+r)// 2
            print(f'l:{l} r:{r} m:{m} m_ele:{nums[m]}')

            if target == nums[l]:
                return l

            if target == nums[r]:
                return r

            if nums[m] == target:
                return m
            elif nums[m] > target:
                if nums[m] <= nums[r]:
                    r = m - 1
                else:
                    if target > nums[r]:
                        r = m - 1
                    else:
                        l = m+1
            else:
                ## nums[m] < target -> go towards bigger nums
                # if nums[m] <= nums[r]:
                #     if target > nums[r] and target <= nums[l]:
                #         r = m - 1
                #     else:
                #         l = m + 1
                # else:
                #     r = m -1
                if target < nums[r]:
                    l = m + 1
                elif target > nums[r] and target> nums[l]:
                    l = m + 1
                else:
                    r = m - 1

        print(f'l:{l} r:{r} m:{m} m_ele:{nums[m]}')
        return -1