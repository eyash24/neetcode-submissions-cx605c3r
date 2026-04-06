class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_present = False

        for i in nums:
            if i == 0 and not zero_present:
                zero_present = True
                continue
            elif i == 0 and zero_present:
                product *= 0
            else:
                product *= i
        
        req_list = []
        for i in nums:
            if zero_present and i != 0:
                req_list.append(0)
            elif i == 0 :
                req_list.append(product)
            else:
                req_list.append(int(product / i))
        
        return req_list
