class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # using 2 pointer 
        i,j = 0, len(heights) -1
        max_quantity = 0

        while i<j:
            lower_limit = min(heights[i], heights[j])
            distance = j-i
            quantity = lower_limit * distance
            max_quantity = max(max_quantity, quantity)

            if heights[i] < heights[j]:
                i+= 1
            else:
                j-= 1
        
        return max_quantity
