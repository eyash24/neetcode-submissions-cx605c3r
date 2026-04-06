class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        for i,h1 in enumerate(heights):
            for j,h2 in enumerate(heights):
                if i==j:
                    continue
                area = (abs(i-j))*min(h1,h2)
                max_area = max(area, max_area)
        return max_area