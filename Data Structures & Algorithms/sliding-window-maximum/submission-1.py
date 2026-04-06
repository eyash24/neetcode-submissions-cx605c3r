class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # print(nums, k)
        window = nums[:k]
        # print(window)
        count = {}
        for i in window:
            count[i] = 1 + count.get(i, 0)

        # print(count)
        
        max_list = []
        max_list.append(max(window))

        for j in range(1, len(nums)-k+1):
            w0_ele = nums[j-1]
            wj_ele = nums[j+k-1]
            # print("max list: ", max_list)
            # print('w0_ele: ', w0_ele, 'wj_ele: ', wj_ele)

            count[wj_ele] = 1+count.get(w0_ele, 0)
            count[w0_ele] -= 1

            if count[w0_ele] == 0:
                count.pop(w0_ele)

            if max_list[j-1] < wj_ele:
                max_list.append(wj_ele)
            else:
                max_list.append(max(nums[j: k+j]))

        
        return max_list