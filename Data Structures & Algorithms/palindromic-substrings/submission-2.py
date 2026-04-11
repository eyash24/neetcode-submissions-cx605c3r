class Solution:
    def countSubstrings(self, s: str) -> int:
        sum_palin = 0
        limit = len(s)
        sum_palin += limit
        
        for i, ch in enumerate(s):
            odd = ch
            j=1
            while i-j >= 0 and i+j < limit:
                odd = s[i-j: i+j+1]
                # print('o',i,odd, 1+2*j)
                if odd == odd[::-1]:
                    sum_palin += 1
                j += 1
            
            even = ch
            k = 1
            while i-k+1 >=0 and i+k < limit:
                even = s[i-k+1: i+k+1]
                # print('e',i,even, 2*k)
                if even == even[::-1]:
                    sum_palin += 1
                k+=1

        return sum_palin