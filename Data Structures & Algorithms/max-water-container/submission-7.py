class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s,e = 0, len(heights)-1
        max_water = 0
        while s < e:
            water = (e-s) * min(heights[s], heights[e])
            max_water = max(max_water, water)
            if heights[s] < heights[e]:
                s += 1
            else:
                e -= 1
        
        return max_water