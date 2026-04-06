class Solution:
    def trap(self, height: list[int]) -> int:
        # print(height)
        n_len = len(height)
        if n_len < 3:
            return 0
            
        l,r = 0,1
        total_water = 0

        while l<r and r < n_len-1:
            temp = r
            max_r = r
            occupied = 0
            occupied_max = 0
            while temp < n_len:
                occupied += height[temp]
                if height[temp] >= height[l]:
                    max_r = temp
                    occupied_max = occupied
                    break
                if height[temp] >= height[max_r]:
                    occupied_max = occupied
                    max_r = temp
                
                temp += 1

            occupied_max -= height[max_r]
            area = (max_r-l-1)*(min(height[max_r], height[l]))
            avail = area - occupied_max
            # print()
            # print("l,max_r: ", l,max_r)
            # print("Area: ", area)
            # print("Occupied_max: ", occupied_max)
            # print("Avail: ", avail)

            r = max_r
            if avail > 0 and l != r-1:
                total_water += avail
            
            l = r
            r += 1

        return total_water