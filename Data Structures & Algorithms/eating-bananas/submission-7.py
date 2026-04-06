def get_hrs(k, piles):
    hrs = 0

    for p in piles:
        hrs += p // k
        if p % k != 0:
            hrs += 1

    return hrs

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_max = max(piles)
        # print(f'piles: {piles}\n h:{h}')

        l, r = 1,k_max
        tracker = None

        while l <= r:
            # print(f'l: {l}, r: {r}')
            k = (l+r) // 2
            hrs = get_hrs(k, piles)

            if hrs <= h:
                if tracker is None:
                    tracker = [k,hrs]
                elif hrs >= tracker[1]:
                    tracker = [k, hrs] 

            # print(f'k: {k}, hrs:{hrs}')

            if hrs > h:
                l = k + 1

            elif hrs <= h:
                r = k - 1

        
        # print("tracker: ", tracker)
    
        return tracker[0]