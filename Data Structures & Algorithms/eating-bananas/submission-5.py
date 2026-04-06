import math
def dur_cal(ban, h, k):
    # print(ban, h, k)
    durr = 0

    for b in ban:
        durr += math.ceil(b / k)
    
    # print(durr)
    
    if durr <= h:
        return True
    else:
        return False


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        piles.sort()
        low = 1
        high = piles[-1] -1
        k_found = piles[-1]

        while low <= high:
            mid = low + (high - low) // 2
            
            if dur_cal(piles, h, mid):
                k_found = min(mid, k_found)
                high = mid - 1
            else:
                low = mid + 1
        
        return k_found