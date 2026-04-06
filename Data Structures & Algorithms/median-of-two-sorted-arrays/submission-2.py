class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # print(f'nums1:{nums1} \nnums2:{nums2}')
        combination = []
        div_2 = (len(nums1)+len(nums2)) // 2 

        if (len(nums1)+len(nums2)) % 2 == 0:
            req = [div_2-1, div_2]
        else:
            req = [div_2]
        
        print('req: ', req)
        
        while len(combination) < req[-1]+1:
            # print(f'nums1{nums1} nums2:{nums2}')
            l1, r1 = 0, len(nums1) - 1
            l2, r2 = 0, len(nums2) - 1
            mid_1 = (l1+r1) // 2
            mid_2 = (l2+r2) // 2
            print('')
            if len(nums1) > 0 and len(nums2) > 0:
                if nums1[mid_1] >= nums2[mid_2]:
                    combination.extend(nums2[:mid_2+1])
                    if mid_2+1 < len(nums2):
                        nums2 = nums2[mid_2+1:]
                    else:
                        nums2 = []
                else:
                    combination.extend(nums1[:mid_1+1])
                    if mid_1 + 1< len(nums1):
                        nums1 = nums1[mid_1+1:]
                    else:
                        nums1 = []
            elif len(nums1) > 0 and len(nums2) == 0:
                combination.extend(nums1)
                nums1 = []
            elif len(nums1) == 0 and len(nums2) > 0:
                combination.extend(nums2)
                nums2 = []
            else:
                break

        if len(req) == 1:
            return float(combination[req[-1]])
        else:
            return round(float((combination[req[-1]] + combination[req[-2]]) / 2), 1)
        