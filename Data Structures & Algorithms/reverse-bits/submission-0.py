class Solution:
    def reverseBits(self, n: int) -> int:
        index = 31
        n2 = 0
        while n > 0:
            if n&1 == 1:
                n2 += 1 * 2**index
            index -= 1
            n = n >> 1
        return n2
        



        