class Solution:
    def getSum(self, a: int, b: int) -> int:
        limit = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b:
            res = (a ^ b) & limit
            carry = a & b
            a = res
            b = (carry << 1) & limit
                
        if a <= max_int:
            return a
        else:
            return ~(a^limit)
        