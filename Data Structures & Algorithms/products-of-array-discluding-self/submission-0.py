class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_available = 0
        zero_count = 0

        for n in nums:
            if n == 0:
                zero_available = 1
                zero_count += 1
                if zero_count > 1:
                    product = 0
                continue
            product *= n
    
        if product == 0:
            return [0]*len(nums)
        
        prods = []
        for n in nums:
            if n == 0:
                prods.append(product)
                continue
    
            prods.append(int(product*(1-zero_available)/n))
    
        return prods

        
