class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_reverse = nums[::-1]
        product_start_end = [nums[0]]
        product_end_start = [nums_reverse[0]]
        len_nums = len(nums)
        product = []

        for i in range(1, len_nums):
            product_start_end.append(product_start_end[i-1]*nums[i])
            product_end_start.append(product_end_start[i-1]*nums_reverse[i])
        
        product_end_start = product_end_start[::-1]

        # print(nums,product_start_end)
        # print(nums_reverse,product_end_start)

        product.append(1*product_end_start[1])
        
        for i in range(1, len_nums-1):
            product.append(
                product_start_end[i-1] * product_end_start[i+1]
            )

        product.append(product_start_end[-2] * 1)

        return product
            
