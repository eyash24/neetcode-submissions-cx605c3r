class Solution:
    def reverse(self, x: int) -> int:
        lower_bound = (2**31)
        upper_bound = 2**31 -1

        res = 0

        flag = 1 if x > 0 else 0

        if not flag:
            x *= -1
        
        while x > 0:
            re = x % 10
            res = res*10 + re
            x -= re
            x /= 10
        
        print(res)

        

        if not flag and res <= lower_bound:
            return int(res) * -1
        elif flag and res <= upper_bound:
            return int(res)
        else:
            return 0






        