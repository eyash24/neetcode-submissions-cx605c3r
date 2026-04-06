class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # brute force
        max_rec = 0
        limit = len(heights)

        for i1, h1 in enumerate(heights):
            max_rec = max(h1, max_rec)
            min_height = h1

            for i2 in range(i1+1,limit):
                h2 = heights[i2]
                if h2 < min_height:
                    min_height = h2
                
                area = min_height * (i2-i1+1)
                max_rec = max(max_rec, area)
        
        return max_rec

