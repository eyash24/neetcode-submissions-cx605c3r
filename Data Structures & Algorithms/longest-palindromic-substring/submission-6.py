class Solution:
    def longestPalindrome(self, s: str) -> str:

        max_palin = 0
        palin = ''
        limit = len(s)

        if limit < 2:
            return s
        
        for i, ch in enumerate(s):
            odd = ch
            j=1
            while i-j >= 0 and i+j < limit:
                odd = s[i-j: i+j+1]
                # print('o',i,odd, 1+2*j)
                if odd == odd[::-1] and max_palin < 1+2*j:
                    max_palin = 1+2*j
                    palin = odd
                # else:
                #     break
                j += 1
            
            even = ch
            k = 1
            while i-k+1 >=0 and i+k < limit:
                even = s[i-k+1: i+k+1]
                # print('e',i,even, 2*k)
                if even == even[::-1] and max_palin < 2*k:
                    max_palin = 2*k
                    palin = even
                # else:
                #     break
                k+=1

            if palin == "":
                palin = s[0]

        return palin




        
