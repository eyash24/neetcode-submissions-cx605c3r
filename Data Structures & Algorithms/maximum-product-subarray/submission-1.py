class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        tracker = [(i,j,j+1) for j,i in enumerate(nums)]
        # print(f'iteration: 0 tracker: {tracker}')
        max_val = max(nums)
        limit_l, limit_h = 0, len(nums)-1
        
        for i in range(limit_h+1):
            for pos, info in enumerate(tracker):
                ele, c1, c2 = info
                
                
                if c1-1 >= limit_l and c2+1 <= limit_h:
                    t1 = ele*nums[c1-1]
                    c1_new = c1-1

                    t2 = ele*nums[c2]
                    c2_new = c2+1

                    if t1 >= t2:
                        tracker[pos] = (t1, c1_new, c2)
                    else:
                        tracker[pos] = (t2, c1, c2_new)
                    
                elif c1 -1 >= limit_l:
                    tracker[pos] = (ele*nums[c1-1], c1-1, c2)
                
                elif c2 +1 <= limit_h:
                    tracker[pos] = (ele*nums[c2], c1, c2+1)
                
                max_val = max(max_val, tracker[pos][0])
            # print(f'Iteratoin: {i} tracker: {tracker}')
        
        return max_val




                


                 


            
